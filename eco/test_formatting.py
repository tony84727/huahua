from eco.formatting import discord_friendly_message
import unittest


class TestFormatting(unittest.TestCase):
    def test_discord_friendly_message(self):
        self.assertEqual('不偷竊 \n 不破壞道路 \n 不亂丟垃圾 \n 圈地保持距離 \n 一緒に平和にゲームをしましょう \n大鏟\n貨架\n貨櫃\n藝術\n紙業\n回收業\n木漿壓縮\n腳踏車\n有色建材\n車輛上色\nnext food\n技能卷軸無技能書 ', discord_friendly_message(
            '不偷竊 <br> 不破壞道路 <br> 不亂丟垃圾 <br> 圈地保持距離 <br> <b><color=red>一緒に平和にゲームをしましょう</b></color> <i><br>大鏟<br>貨架<br>貨櫃<br>藝術<br>紙業<br>回收業<br>木漿壓縮<br>腳踏車<br>有色建材<br>車輛上色<br>next food<br>技能卷軸無技能書 </i>'))


if __name__ == '__main__':
    unittest.main()
