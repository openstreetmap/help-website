+++
type = "question"
title = "wireshark lua dissector -- how to query the name of the capture file?"
description = '''I am writing a lua dissector for a propietary protocol. The packets include embedded .png files that I would like to write to an output folder named &quot;ImageDump_&amp;lt;capturefilename&amp;gt;&quot;. Is there a way in lua to query the name of the current capture file being loaded?'''
date = "2015-08-04T18:42:00Z"
lastmod = "2015-08-04T19:09:00Z"
weight = 44843
keywords = [ "lua", "dissector", "capture", "filename" ]
aliases = [ "/questions/44843" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark lua dissector -- how to query the name of the capture file?](/questions/44843/wireshark-lua-dissector-how-to-query-the-name-of-the-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44843-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a lua dissector for a propietary protocol. The packets include embedded .png files that I would like to write to an output folder named "ImageDump_&lt;capturefilename&gt;". Is there a way in lua to query the name of the current capture file being loaded?</p></div><div id="question-tags" class="tags-container tags">lua dissector capture filename</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Aug '15, 18:42</strong></p><img src="https://secure.gravatar.com/avatar/0e669f5129ac13bdba3262abcfbaa92b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mfbaker&#39;s gravatar image" /><p>mfbaker<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mfbaker has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Aug '15, 18:44</p></div></div><div id="comments-container-44843" class="comments-container"></div><div id="comment-tools-44843" class="comment-tools"></div><div class="clear"></div><div id="comment-44843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44845"></span>

<div id="answer-container-44845" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44845-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not that I know of.</p><p>Are you doing this in tshark, or wireshark, or both?</p><p>If you're doing this in Wireshark, then you should probably not do it automatically but instead only when the user tells you to, like through a menu command - in which case you could have them type a folder name to use in a dialog window when they select that menu item. (i.e., have the Lua script add a menu item called "Export PNG...", and have that create a window for text input of the folder name)</p><p>If you're doing this in tshark, then you should probably still not do it automatically, but only if they load your script with the "<code>tshark -r [capture_filename] -X lua_script:png_export.lua</code>" command switch - in which case you can have an argument passed to your script as well, by doing "<code>tshark -r [capture_filename] -X lua_script:png_export.lua -X lua_script1:[folder_name]</code>".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '15, 19:09</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-44845" class="comments-container"><span id="44846"></span><div id="comment-44846" class="comment"><div id="post-44846-score" class="comment-score"></div><div class="comment-text"><p>It is only for wireshark. I did add a menu item to only write the image files if a menu item is selected to do so:</p><pre><code>local ImageDumpOn = false
local ImageDumpMenuText = &quot;Toggle RFBTV Image Dump&quot;

local function toggleImageDump() 
    if ImageDumpOn then 
        ImageDumpOn = false
    else 
        ImageDumpOn = true
    end
end

register_menu(ImageDumpMenuText, toggleImageDump, MENU_TOOLS_UNSORTED)</code></pre></div><div id="comment-44846-info" class="comment-info"><span class="comment-age">(04 Aug '15, 19:18)</span> mfbaker</div></div><span id="45427"></span><div id="comment-45427" class="comment"><div id="post-45427-score" class="comment-score"></div><div class="comment-text"><p>I am writing a wireshark lua dissector for a propietary protocol, and am still looking for an answer to the question I posted about a month ago. Is there a way in lua to query the name of the current capture file being loaded? The packets include embedded .png files that I would like to write to an output folder named "ImageDump_&lt;capturefilename&gt;".</p></div><div id="comment-45427-info" class="comment-info"><span class="comment-age">(27 Aug '15, 17:07)</span> mfbaker</div></div></div><div id="comment-tools-44845" class="comment-tools"></div><div class="clear"></div><div id="comment-44845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

