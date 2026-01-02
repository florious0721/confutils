from functools import partial, reduce
from pathlib import Path
from setting import *

import sys

Deco = Appearance.Decoration

def bool2str(b: bool) -> str:
    return str(b).lower()

def deco_conf() -> str:
    return f'''general {{
    border_size = {Appearance.Border}
    no_border_on_floating = {bool2str(not Appearance.BorderFloating)}

    gaps_in = {Appearance.GapsWD}
    gaps_out = {Appearance.GapsWD_MON}
    float_gaps = {Appearance.GapsWD_MON}
    gaps_workspaces = {Appearance.GapsWS}
}}
decoration {{
    rounding = {Deco.Rounding}
    rounding_power = {Deco.RoundingPower}

    active_opacity = {Deco.Opacity.Active}
    fullscreen_opacity = {Deco.Opacity.Fullscreen}
    inactive_opacity = {Deco.Opacity.Inactive}

    dim_around = {Deco.Dim.Around:.1f}
    dim_inactive = {bool2str(Deco.Dim.Inactive)}
    dim_modal = {bool2str(Deco.Dim.ModalParent)}
    dim_special = {Deco.Dim.Special:.1f}
    dim_strength = {Deco.Dim.Strength:.1f}

    #screen_shader = {Deco.Shader}

    blur {{
        enabled = {bool2str(Deco.Blur.Enabled)}
    }}

    shadow {{
        enabled = {bool2str(Deco.Shadow.Enabled)}
    }}
}}
misc {{
    font_family = {Appearance.Font.Family}
}}
'''

def behav_conf() -> str:
    return f'''general {{
    layout = {Behaviour.DefaultLayout}
    no_focus_fallback = {bool2str(not Behaviour.FocusFallback)}
    resize_on_border = {bool2str(Behaviour.ResizeOnBorder)}
    extend_border_grab_area = {Behaviour.ExtendBorderDragArea}
    hover_icon_on_border = {bool2str(Behaviour.HoverIconOnBorder)}
    resize_corner = {Behaviour.ResizeCorner}

    snap {{
        enabled = {bool2str(Behaviour.Snap.Enabled)}
        window_gap = {Behaviour.Snap.StrengthWD}
        monitor_gap = {Behaviour.Snap.StrengthMON}
        border_overlap = {bool2str(Behaviour.Snap.BorderOverlap)}
        respect_gaps = {bool2str(Behaviour.Snap.RespectGaps)}
    }}
}}
decoration {{
    border_part_of_window = {bool2str(Behaviour.BorderAsPartOfWindow)}
}}
input {{
    float_switch_override_focus = {Behaviour.FocusOnFloatSwitch}
    focus_on_close = {Behaviour.FocusOnClose}
    follow_mouse = {Behaviour.FocusFollowMouse}
}}
misc {{
    disable_autoreload = {bool2str(not Behaviour.AutoReload)}
    focus_on_activate = {bool2str(Behaviour.AllowFocusRequest)}

    mouse_move_enables_dpms = {bool2str(Behaviour.DPMS.MouseMoveToEnable)}
    key_press_enables_dpms = {bool2str(Behaviour.DPMS.KeyPressToEnable)}
}}
cursor {{
    inactive_timeout = {Behaviour.Cursor.InactiveTimeout:.1f}
}}
xwayland {{
    enabled = {bool2str(Behaviour.XWayland.Enabled)}
}}
'''

Touchpad = Input.Touchpad
def input_conf() -> str:
    return f'''input {{
    #kb_file = {Input.KBFile}
    kb_layout = {Input.KBLayout}
    kb_model = {Input.KBModel}
    kb_options = {Input.KBOptions}
    kb_rules = {Input.KBRules}
    kb_variant = {Input.KBVariant}

    numlock_by_default = {bool2str(Input.NumlockByDefault)}
    repeat_delay = {Input.RepeatDelay}
    repeat_rate = {Input.RepeatRate}

    accel_profile = {Input.AccelProfile}
    force_no_accel = {bool2str(Input.ForceNoAccel)}
    left_handed = {bool2str(Input.LeftHanded)}
    natural_scroll = {bool2str(Input.NaturalScroll)}
    scroll_button_lock = {bool2str(Input.ScrollButtonLock)}
    scroll_button = {Input.ScrollButton}
    scroll_factor = {Input.ScrollFactor:.1f}
    scroll_method = {Input.ScrollMethod}
    #scroll_points = {Input.ScrollPoints}
    sensitivity = {Input.Sensitivity}

    resolve_binds_by_sym = {bool2str(Input.ResolveBindsBySym)}

    touchpad {{
        disable_while_typing = {bool2str(Touchpad.DisableWhileTyping)}
        middle_button_emulation = {bool2str(Touchpad.MiddleButtonEmulation)}
        natural_scroll = {bool2str(Touchpad.NaturalScroll)}
        tap-and-drag = {bool2str(Touchpad.TapAndDrag)}
        tap_button_map = {Touchpad.TapButtonMap}
        tap-to-click = {bool2str(Touchpad.TapToClick)}
    }}
}}
'''

def render_conf() -> str:
    return f'''general {{
    allow_tearing = {bool2str(Render.AllowTearing)}
}}
misc {{
    vfr = {bool2str(Render.VFR)}
    vrr = {Render.AdaptiveSync}
}}
render {{
    direct_scanout = {Render.DirectScanout}
    new_render_scheduling = {bool2str(Render.TripleBuffering)}

    cm_enabled = {bool2str(Render.ColorManagement.Enabled)}
}}
'''

def bind_conf() -> str:
    Action = Keybind.Action
    Para = Keybind.Para

    def focus(p) -> str:
        if p == Para.Direction.NEXT:
            return 'cyclenext'
        elif p == Para.Direction.PREV:
            return 'cyclenext, prev'
        elif p == Para.Direction.RIGHT:
            return 'movefocus, r'
        elif p == Para.Direction.DOWN:
            return 'movefocus, d'
        elif p == Para.Direction.LEFT:
            return 'movefocus, l'
        elif p == Para.Direction.UP:
            return 'movefocus, u'
        else:
            raise ValueError()
    def ws(a: str, p) -> str:
        if p == Para.Direction.NEXT:
            return f'{a}, +1'
        elif p == Para.Direction.PREV:
            return f'{a}, -1'
        elif isinstance(p, str):
            return f'{a}, name:{p}'
        else:
            return f'{a}, {p}'
    def move(p) -> str:
        if p == Para.Direction.MOUSE:
            return 'movewindow'
        else:
            raise Exception('Unimplement')
    def resize(p) -> str:
        if p == Para.Direction.MOUSE:
            return 'resizewindow'
        else:
            raise Exception('Unimplement')

    def bind(t: tuple) -> str:
        cmd = 'bind'
        mod = t[0]
        sym = t[1]
        act = t[2]
        para = t[3]

        if para == Para.Direction.MOUSE: cmd = 'bindm'

        mods = []
        for i in Keybind.Mod:
            if mod & i.value: mods.append(i.name)

        statemap = {
            Para.State.MAXIMIZED: 'fullscreen, 1',
            Para.State.FULLSCREEN: 'fullscreen, 0',
            Para.State.FLOATING: 'togglefloating',
            Para.State.PINNED: 'pin',
        }
        actmap = {
            Action.FOCUS: focus,
            Action.FOCUS_WS: partial(ws, 'workspace'),
            Action.EXEC: lambda p: f'exec, {p}',
            Action.CLOSE: lambda p: 'killactive',
            Action.KILL: lambda p: 'forcekillactive',
            Action.QUIT: lambda p: 'exit',
            Action.MOVE: move,
            Action.MOVE_TO_WS: partial(ws, 'movetoworkspace'),
            Action.RESIZE: resize,
            Action.RESIZE_KR: lambda p: 'resizewindow 1',
            Action.RECONF: lambda p: 'exec, hyprctl reload',
            Action.TOGGLE_WINDOW_STATE: lambda p: statemap[p],
            #Action.TOGGLE_TOUCHPAD: '',
            #Action.TOGGLE_DPMS: lambda p: 'hyprctl dispatch dpms toggle',
        }

        return f'{cmd} = {'&'.join(mods)}, {sym}, {actmap[act](para)}\n'

    return reduce(lambda k, c: k + bind(c), Keybind.Binds, '')

def main():
    dir = Path(sys.argv[1])
    confs = [
        (deco_conf, 'deco.conf'),
        (behav_conf, 'behav.conf'),
        (input_conf, 'input.conf'),
        (render_conf, 'render.conf'),
        (bind_conf, 'bind.conf'),
    ]
    for i in confs:
        with open(dir/i[1], 'wt') as f:
            f.write(i[0]())
    with open(dir/'hyprland.conf', 'wt') as f:
        for i in confs:
            f.write(f'source = {i[1]}\n')
        f.write(f'''bind = SUPER&ALT, Z, exit
bind = SUPER, Return, exec, {Apps.Terminal}
animations {{
    enabled = false
}}
misc {{
    force_default_wallpaper = 1
}}
exec-once = wayinit.sh
exec-shutdown = wayterm.sh
''')

main()
