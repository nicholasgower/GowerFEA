

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.5
import QtQuick.Controls 6.5
import FEA2D

Rectangle {
    id: rectangle
    width: Constants.width
    height: Constants.height
    visible: true

    color: Constants.backgroundColor

    Button {
        id: button
        text: qsTr("Press me")
        anchors.verticalCenter: parent.verticalCenter
        highlighted: false
        flat: false
        checkable: true
        anchors.horizontalCenter: parent.horizontalCenter

        Connections {
            target: button
            onClicked: animation.start()
        }
    }

    Text {
        id: label
        text: qsTr("Hello FEA2D")
        anchors.top: button.bottom
        font.family: Constants.font.family
        anchors.topMargin: 45
        anchors.horizontalCenter: parent.horizontalCenter

        SequentialAnimation {
            id: animation

            ColorAnimation {
                id: colorAnimation1
                target: rectangle
                property: "color"
                to: "#2294c6"
                from: Constants.backgroundColor
            }

            ColorAnimation {
                id: colorAnimation2
                target: rectangle
                property: "color"
                to: Constants.backgroundColor
                from: "#2294c6"
            }
        }
    }

    TabBar {
        id: tabBar
        x: 1530
        y: 188
        width: 240
    }

    TabBar {
        id: tabBar1
        x: 272
        y: 0
        width: 240
    }

    ToolBar {
        id: toolBar
        x: 134
        y: 708
        width: 360
    }

    Flickable {
        id: flickable1
        x: 0
        y: 47
        width: 296
        height: 1033
        flickableDirection: Flickable.HorizontalFlick

        Frame {
            id: frame
            x: 0
            y: 99
            width: 246
            height: 461
            anchors.left: parent.left
            anchors.leftMargin: 0

            ScrollView {
                id: scrollView
                x: 0
                y: 11
                width: 222
                height: 222

                Rectangle {

                    id: sidebarSetting1
                    x: 11
                    y: 13
                    width: 200
                    height: 30
                    color: "#ffffff"

                    TextInput {
                        id: textInput
                        x: 126
                        y: 5
                        width: 66
                        height: 20
                        text: qsTr("1")
                        font.pixelSize: 12
                        horizontalAlignment: Text.AlignRight
                        verticalAlignment: Text.AlignVCenter
                    }

                    Text {
                        id: text1
                        x: 8
                        y: 7
                        text: qsTr("Object Thickness")
                        font.pixelSize: 12
                    }
                }

                Rectangle {
                    id: sidebarSetting2
                    x: 11
                    y: 43
                    width: 200
                    height: 30
                    color: "#ffffff"
                    TextInput {
                        id: textInput1
                        x: 126
                        y: 5
                        width: 66
                        height: 20
                        text: qsTr("1")
                        font.pixelSize: 12
                        horizontalAlignment: Text.AlignRight
                        verticalAlignment: Text.AlignVCenter
                    }

                    Text {
                        id: text2
                        x: 8
                        y: 7
                        text: qsTr("Mesh Size")
                        font.pixelSize: 12
                    }
                }

                Rectangle {
                    id: sidebarSetting3
                    x: 11
                    y: 73
                    width: 200
                    height: 30
                    color: "#ffffff"

                    Text {
                        id: text3
                        x: 8
                        y: 7
                        text: qsTr("Use Mesh Node count")
                        font.pixelSize: 12
                    }

                    CheckBox {
                        id: checkBox
                        x: 172
                        y: -3
                        width: 28
                        height: 35
                    }
                }

                Rectangle {
                    id: sidebarSetting4
                    x: 11
                    y: 103
                    width: 200
                    height: 30
                    color: "#ffffff"
                    TextInput {
                        id: textInput2
                        x: 126
                        y: 5
                        width: 66
                        height: 20
                        text: qsTr("1")
                        font.pixelSize: 12
                        horizontalAlignment: Text.AlignRight
                        verticalAlignment: Text.AlignVCenter
                    }

                    Text {
                        id: text4
                        x: 8
                        y: 7
                        text: qsTr("Elastic Modulus")
                        font.pixelSize: 12
                    }
                }

                Rectangle {
                    id: sidebarSetting5
                    x: 11
                    y: 133
                    width: 200
                    height: 30
                    color: "#ffffff"
                    TextInput {
                        id: textInput3
                        x: 126
                        y: 5
                        width: 66
                        height: 20
                        text: qsTr("0.5")
                        font.pixelSize: 12
                        horizontalAlignment: Text.AlignRight
                        verticalAlignment: Text.AlignVCenter
                    }

                    Text {
                        id: text5
                        x: 8
                        y: 7
                        text: qsTr("Poisson Ratio")
                        font.pixelSize: 12
                    }
                }
            }
        }
    }

    ProgressBar {
        id: progressBar
        x: 350
        y: 1046
        value: 0.5
    }

    Row {
        id: row
        x: 332
        y: 136
        width: 200
        height: 400
    }

    Loader {
        id: loader
        x: 515
        y: 420
        width: 200
        height: 200
    }

    TabBar {
        id: tabBar2
        x: 0
        width: 1920
        height: 48
        anchors.top: parent.top
        anchors.topMargin: 0

        TabButton {
            id: tabButton
            y: 0
            text: qsTr("Tab Button")
            anchors.left: parent.left
            anchors.leftMargin: -1
        }
    }
    states: [
        State {
            name: "clicked"
            when: button.checked

            PropertyChanges {
                target: label
                text: qsTr("Button Checked")
            }
        }
    ]
}

/*##^##
Designer {
    D{i:0}D{i:31}D{i:32;invisible:true}
}
##^##*/
