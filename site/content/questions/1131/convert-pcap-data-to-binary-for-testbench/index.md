+++
type = "question"
title = "Convert pcap data to binary for testbench"
description = '''Hi, I&#x27;m trying to convert a pcap file to binary for use in testing in a new product, I&#x27;m working on. I figured the best thing to do was 1...save the file in a .k12 text file, where I get the following format of text file... +---------+---------------+----------+ 09:19:40,736,392 ETHER |0 |00|05|47|0...'''
date = "2010-11-26T08:34:00Z"
lastmod = "2015-06-01T20:43:00Z"
weight = 1131
keywords = [ "k12" ]
aliases = [ "/questions/1131" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Convert pcap data to binary for testbench](/questions/1131/convert-pcap-data-to-binary-for-testbench)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1131-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to convert a pcap file to binary for use in testing in a new product, I'm working on. I figured the best thing to do was</p><p>1...save the file in a .k12 text file, where I get the following format of text file...</p><p>+---------+---------------+----------+ 09:19:40,736,392 ETHER |0 |00|05|47|02|99|c6|00|03|fa| ........etc etc</p><p>2...I parse this text file using a perl script to get 00 05 47 02 99 c6 00 03 fa ........etc etc</p><p>3...I then convert this to serial binary data format which I need</p><p>000000000000010101000111000000101001 ........etc, etc, which is just the binary format of the hex data.</p><p>When I this is read by the internet device, I'm working on, I would have expected it to recognise this a valid internet traffic, but it doesn't. I've a few questions...</p><p>Does the .k12 file contain valid data or are there other headers, that I need to remove before converting it to binary?</p><p>Are there any endian issues that I need to be aware of when parsing the .k12 file?</p><p>Alternatively, is there any other method of extracting the data from wireshark into this format?</p><p>Regards Mike</p></div><div id="question-tags" class="tags-container tags">k12</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '10, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/2cd987f001592119fffae11c35779498?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stenasc&#39;s gravatar image" /><p>stenasc<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stenasc has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Nov '10, 20:06</p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p>lchappell ♦<br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span></p></div></div><div id="comments-container-1131" class="comments-container"></div><div id="comment-tools-1131" class="comment-tools"></div><div class="clear"></div><div id="comment-1131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="1134"></span>

<div id="answer-container-1134" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1134-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A pcap file is "binary" in the sense that it's not a text file. What are you trying to do with the packets in the pcap file? Transmit them on a network of the same type as the network on which they were captured? If so, then the "Traffic generators" section of <a href="http://wiki.wireshark.org/Tools">the Tools page on the Wireshark Wiki</a> lists some tools you can use to do that, such as tcpreplay and bittwist.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '10, 23:23</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-1134" class="comments-container"><span id="1143"></span><div id="comment-1143" class="comment"><div id="post-1143-score" class="comment-score"></div><div class="comment-text"><p>What I'm trying to do is represent the actual packets data as binary which I feed serially into an ethernet phy on an fpga. In the simulation, I would be able to check if the phy is working correctly, but at the moment, the phy is telling me that the data I'm feeding it is invalid.</p></div><div id="comment-1143-info" class="comment-info"><span class="comment-age">(28 Nov '10, 15:33)</span> stenasc</div></div><span id="1168"></span><div id="comment-1168" class="comment"><div id="post-1168-score" class="comment-score"></div><div class="comment-text"><p>The easiest way to do that might be to write your own program that reads Ethernet pcap files and writes out the raw packet data in the appropriate format (to a file or to the FPGA). For help on doing this, you should probably ask the [email protected] or [email protected] mailing lists.</p></div><div id="comment-1168-info" class="comment-info"><span class="comment-age">(29 Nov '10, 16:52)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-1134" class="comment-tools"></div><div class="clear"></div><div id="comment-1134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1138"></span>

<div id="answer-container-1138" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1138-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Best way would be to use <a href="http://www.lua.org">Lua</a> to do it for you</p><ol><li>Make sure your wireshark/tshark is compiled with lua</li><li>Enable lua by editing /usr/share/wireshark/init.lua</li><li>Create file test.lua with contents from source below</li><li>Run tshark with lua script like below</li></ol><pre><code>[[email protected] ~]$ tshark -n -r tmp.pcap -Xlua_script:./test.lua   -w /dev/null
Lua started
Found addr 00:50:56:c0:00:08 in packet # 1 Bin: 000000000101000001010110110000000000000000001000</code></pre><code></code><p>For more info on how to extend wireshark with lua see this guide <a href="http://www.cacetech.com/sharkfest.09/DT06_Bjorlykke_Lua%20Scripting%20in%20Wireshark.pdf">Lua Scripting in Wireshark</a></p><pre><code>-- Start test.lua
print(&quot;Lua started&quot;)

local hex_tbl = {
        [&quot;0&quot;] = &quot;0000&quot;,
        [&quot;1&quot;] = &quot;0001&quot;,
        [&quot;2&quot;] = &quot;0010&quot;,
        [&quot;3&quot;] = &quot;0011&quot;,
        [&quot;4&quot;] = &quot;0100&quot;,
        [&quot;5&quot;] = &quot;0101&quot;,
        [&quot;6&quot;] = &quot;0110&quot;,
        [&quot;7&quot;] = &quot;0111&quot;,
        [&quot;8&quot;] = &quot;1000&quot;,
        [&quot;9&quot;] = &quot;1001&quot;,
        [&quot;a&quot;] = &quot;1010&quot;,
        [&quot;b&quot;] = &quot;1011&quot;,
        [&quot;c&quot;] = &quot;1100&quot;,
        [&quot;d&quot;] = &quot;1101&quot;,
        [&quot;e&quot;] = &quot;1110&quot;,
        [&quot;f&quot;] = &quot;1111&quot;
}

function to_bin(s)
        -- Convert ethernet address to binary
        -- Logic stolen from http://www.dialectronics.com/Lua/code/BinDecHex.shtml
        --
        local ret = &quot;&quot;
        local i = 0

        for i in string.gfind(s, &quot;.&quot;) do
                if i ~= &quot;:&quot; then
                        i = string.lower(i)
                        ret = ret..hex_tbl[i]
                end
        end
        return ret
end

eth_src_extr = Field.new(&quot;eth.src&quot;)
local eth_listener = Listener.new()

function eth_listener.packet(pinfo, tvb, userdata)
        local eth_addr = eth_src_extr()
        if eth_addr then
                local eth_addr_str = tostring(eth_addr)
                print(&quot;Found addr &quot;.. eth_addr_str .. &quot; in packet # &quot; .. pinfo.number .. &quot; Bin: &quot; ..to_bin(eth_addr_str))
        end
end

-- End test.lua</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '10, 15:10</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p>izopizo<br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-1138" class="comments-container"></div><div id="comment-tools-1138" class="comment-tools"></div><div class="clear"></div><div id="comment-1138-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42821"></span>

<div id="answer-container-42821" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42821-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>stuck with the same problem, here is how i fixed it. Export the packet as a "C" array. Then replace the "static const unsigned char" with "reg [7:0]" (assuming verilog), replace the 0x of all hex numbers with 8'h and precede all the opening curly brackets with a single quote. This should let you place it directly in to a verilog file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '15, 20:43</strong></p><img src="https://secure.gravatar.com/avatar/546af4a5e6ffc1969c2c8635de4b4b3b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JDK&#39;s gravatar image" /><p>JDK<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JDK has no accepted answers">0%</span></p></div></div><div id="comments-container-42821" class="comments-container"></div><div id="comment-tools-42821" class="comment-tools"></div><div class="clear"></div><div id="comment-42821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

