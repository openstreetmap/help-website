+++
type = "question"
title = "Lua dissector is not invoked when using tshark (Windows 10)"
description = '''I have a bunch of dissectors I wrote in Lua, which I used in the Wireshark GUI so far - now I want to use them with tshark (under Windows 10). The problem is that one of my dissectors does not work when invoked in tshark (even though it gets initialized). tshark does not output any packets at all, e...'''
date = "2017-03-08T05:29:00Z"
lastmod = "2017-03-08T05:29:00Z"
weight = 59923
keywords = [ "lua", "dissector", "tshark" ]
aliases = [ "/questions/59923" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua dissector is not invoked when using tshark (Windows 10)](/questions/59923/lua-dissector-is-not-invoked-when-using-tshark-windows-10)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59923-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a bunch of dissectors I wrote in Lua, which I used in the Wireshark GUI so far - now I want to use them with tshark (under Windows 10). The problem is that one of my dissectors does not work when invoked in tshark (even though it gets initialized). tshark does not output any packets at all, even though all other dissectors are working fine. I am calling the dissector from one of my other dissectors with</p><pre><code>[...]
info(&quot;calling dissector&quot;)
getDissector(&quot;myproto&quot;):call(payload_tvb, packet_info, tree)</code></pre><p>while the dissector itself looks like:</p><pre><code>function myproto.init()
    info(&quot;Initialization of myproto dissector&quot;)
end
function myproto.dissector(buffer, packet_info, tree)
    info(&quot;dissector successfully called&quot;)
    [...]
end</code></pre><p>Nothing special, actually. From the log, I can see that the dissector gets initialized. But when I open a .pcapng file with tshark, then the log message "dissector successfully called" never gets printed, while in the Wireshark GUI, it does.</p><p>I am not seeing any error message, so I have no clue what the issue might be. The getDissector function call does not return nil, I checked that. The lua files are placed in my AppData\Roaming\Wireshark\plugins directory, and tshark does not seem to have a problem finding them there. Does anybody have an idea what might be wrong with this dissector? Any help is appreciated, thanks in advance.</p></div><div id="question-tags" class="tags-container tags">lua dissector tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '17, 05:29</strong></p><img src="https://secure.gravatar.com/avatar/00a96bd28fd02417186122229a517000?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patrick_oppermann&#39;s gravatar image" /><p>patrick_oppe...<br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patrick_oppermann has no accepted answers">0%</span></p></div></div><div id="comments-container-59923" class="comments-container"></div><div id="comment-tools-59923" class="comment-tools"></div><div class="clear"></div><div id="comment-59923-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

