from enum import Enum, auto

ENV = {
    'LANG': 'zh_CN.UTF-8',

    #'GTK_IM_MODULE': 'fcitx',
    'QT_IM_MODULE': 'fcitx',
    'XMODIFIERS': '@im=fcitx',
    'INPUT_METHOD': 'fcitx',
    'SDL_IM_MODULE': 'fcitx',
    'GLFW_IM_MODULE': 'ibus',

    'XDG_SESSION_TYPE': 'wayland',

    'XCURSOR_THEME': 'GoogleDot-White', #@reference_tag(cursor_theme)
    'XCURSOR_SIZE': '28',
    'HYPRCURSOR_SIZE': '28',

    'WLR_RENDERER': 'vulkan',

    'GTK_THEME': 'Matcha-dark-sea:dark', #@reference_tag(gtk_theme)

    'QT_AUTO_SCREEN_SCALE_FACTOR': '1',
    'QT_STYLE_OVERRIDE': 'kvantum-dark',

    'CLUTTER_BACKEND': 'wayland',
    'GDK_BACKEND': 'wayland,x11',
    'MOZ_ENABLE_WAYLAND': '1',
    'QT_QPA_PLATFORM': 'wayland',
    'QT_WAYLAND_DISABLE_WINDOWDECORATION': '1',

    'LABWC_UPDATE_ACTIVATION_ENV': '1',
}

class Colors: # RGBA
    FG = (0xff, 0xff, 0xff, 0xff,)
    BG = (0x17, 0x18, 0x1a, 0xff,)
    BGAlt = (0x42, 0x42, 0x42, 0xff,)
    Disable = (0x78, 0x90, 0x9c, 0xff,)

    Blue = (0x42, 0xa5, 0xf5, 0xff,)
    BlueAlt = (0x30, 0x3f, 0x9f, 0xff,)
    Green = (0x66, 0xbb, 0x6a, 0xff,)
    Pink = (0xec, 0x40, 0x7a, 0xff,)
    Yellow = (0xff, 0xeb, 0x3b, 0xff,)

class Apps:
    WM = 'Hyprland'
    Terminal = 'foot'
    PureTerminal = 'foot bash'

    Launcher = 'fuzzel'

    Lock = 'loginctl lock-session'

    VolInc = 'volctl.py +5'
    VolDec = 'volctl.py -5'
    VolMute = 'volctl.py mute'

    Shot = 'shot.sh'
    ShotPartial = 'shot.sh slurp'

class Appearance:
    BorderFloating = True
    Border = 4

    GapsWD = 0
    GapsWD_MON = 0
    GapsWS = 0

    class Decoration:
        Rounding = 0
        RoundingPower = 1.0

        Shader = ''

        class Blur:
            Enabled = False

        class Dim:
            Around = 0.0
            Inactive = False
            ModalParent = False # 使模态框的父窗口暗化
            Special = 0.0 # 特殊工作区打开时屏幕剩余部分的暗化程度
            Strength = 0.0

        class Opacity:
            Active = 1.0
            Fullscreen = 1.0
            Inactive = 0.7

        class Shadow:
            Enabled = False

    class Font:
        Family = 'monospace'


class Behaviour:
    AllowFocusRequest = True
    AutoReload = False

    DefaultLayout = 'master'

    FocusFallback = True
    FocusOnFloatSwitch = 1
    FocusFollowMouse = 2
    FocusOnClose = 0

    BorderAsPartOfWindow = True

    ResizeOnBorder = True
    ExtendBorderDragArea = 4
    HoverIconOnBorder = True
    ResizeCorner = 0

    class Cursor:
        InactiveTimeout = 5.0

    class DPMS:
        MouseMoveToEnable = False
        KeyPressToEnable = True

    class Snap:
        Enabled = False
        StrengthWD = 20
        StrengthMON = 20

        BorderOverlap = False
        RespectGaps = False

    class XWayland:
        Enabled = True

class Input:
    KBFile = ''
    KBLayout = 'cn'
    KBModel = 'pc105'
    KBOptions = ''
    KBRules = ''
    KBVariant = ''

    NumlockByDefault = True
    RepeatDelay = 300
    RepeatRate = 25

    AccelProfile = 'flat'
    ForceNoAccel = False
    LeftHanded = False
    NaturalScroll = False
    ScrollButtonLock = False
    ScrollButton = 0
    ScrollFactor = 1.0
    ScrollMethod = '2fg'
    ScrollPoints = ''
    Sensitivity = 0.39

    ResolveBindsBySym = False # hyprland

    class Touchpad:
        DisableWhileTyping = True
        MiddleButtonEmulation = False
        NaturalScroll = True
        TapAndDrag = True
        TapButtonMap = 'lrm'
        TapToClick = True

class Keybind:
    class Mod(Enum):
        SUPER = 0x1
        SHIFT = 0x2
        CTRL = 0x4
        ALT = 0x8
    class Action(Enum):
        FOCUS = 0
        FOCUS_WS = auto()

        EXEC = auto()
        CLOSE = auto()
        KILL = auto()
        QUIT = auto()

        MOVE = auto()
        MOVE_TO_WS = auto()
        RESIZE = auto()
        RESIZE_KR = auto()

        RECONF = auto()

        TOGGLE_WINDOW_STATE = auto()
        TOGGLE_TOUCHPAD = auto()
        TOGGLE_DPMS = auto()
    class Para:
        class Direction(Enum):
            NEXT = 0
            PREV = auto()

            RIGHT = auto()
            DOWN = auto()
            LEFT = auto()
            UP = auto()

            MOUSE = auto()

        class State(Enum):
            MAXIMIZED = 0
            FULLSCREEN = auto()
            FLOATING = auto()
            PINNED = auto()

    MainMod = Mod.SUPER.value
    SubMod = Mod.SUPER.value | Mod.CTRL.value
    ExtMod = Mod.SUPER.value | Mod.ALT.value
    RevMod = Mod.SUPER.value | Mod.SHIFT.value

    Binds = [
        (
            MainMod, 'grave',
            Action.RECONF, None,
        ),
        (
            MainMod, 'z',
            Action.CLOSE, None,
        ),

        (
            MainMod, 'w',
            Action.FOCUS, Para.Direction.NEXT,
        ),
        (
            RevMod, 'w',
            Action.FOCUS, Para.Direction.PREV,
        ),
        (
            MainMod, 's',
            Action.FOCUS_WS, Para.Direction.NEXT,
        ),
        (
            RevMod, 's',
            Action.FOCUS_WS, Para.Direction.PREV,
        ),
        (
            MainMod, 'd',
            Action.MOVE_TO_WS, Para.Direction.NEXT,
        ),
        (
            RevMod, 'd',
            Action.MOVE_TO_WS, Para.Direction.PREV,
        ),

        (
            MainMod, 'q',
            Action.TOGGLE_WINDOW_STATE, Para.State.MAXIMIZED,
        ),
        (
            SubMod, 'q',
            Action.TOGGLE_WINDOW_STATE, Para.State.FULLSCREEN,
        ),
        (
            MainMod, 'a',
            Action.TOGGLE_WINDOW_STATE, Para.State.FLOATING,
        ),
        (
            SubMod, 'a',
            Action.TOGGLE_WINDOW_STATE, Para.State.PINNED,
        ),

        (
            MainMod, 'mouse:272',
            Action.MOVE, Para.Direction.MOUSE,
        ),
        (
            MainMod, 'mouse:273',
            Action.RESIZE, Para.Direction.MOUSE,
        ),
        (
            SubMod, 'mouse:273',
            Action.RESIZE_KR, Para.Direction.MOUSE,
        ),

        (
            SubMod, 'Return',
            Action.EXEC, Apps.PureTerminal,
        ),
        (
            ExtMod, 'Return',
            Action.EXEC, 'tmux-attach.sh',
        ),
        (
            MainMod, 'l',
            Action.EXEC, Apps.Lock,
        ),
        (
            MainMod, 'r',
            Action.EXEC, Apps.Launcher,
        ),
        (
            0, 'XF86AudioLowerVolume',
            Action.EXEC, Apps.VolDec,
        ),
        (
            0, 'XF86AudioRaiseVolume',
            Action.EXEC, Apps.VolInc,
        ),
        (
            0, 'XF86AudioMute',
            Action.EXEC, Apps.VolMute,
        ),
        (
            MainMod, 'Print',
            Action.EXEC, Apps.Shot,
        ),
        (
            SubMod, 'Print',
            Action.EXEC, Apps.ShotPartial,
        ),
        (
            0, 'XF86Cut',
            Action.EXEC, Apps.Shot,
        ),
        (
            SubMod & ~MainMod, 'XF86Cut',
            Action.EXEC, Apps.ShotPartial,
        ),
        (
            MainMod, 'k',
            Action.EXEC, 'passmenu.sh gui type',
        ),
        (
            SubMod, 'k',
            Action.EXEC, 'passmenu.sh gui',
        ),
    ]

class Render:
    AllowTearing = False
    DirectScanout = 2 # auto
    TripleBuffering = False

    VFR = True
    AdaptiveSync = 1

    class ColorManagement:
        Enabled = True
