+++
type = "question"
title = "Lua script to write the source address to text file when wireshark finds a keyword on live capture not working"
description = '''Hi, I am new to wireshark, tshark and lua. try to capture all uri which contains &quot;abc&quot; to text file automatically. the following code does work and i can hear beep when tshark find a filtered uri. BUT, writing to text file part IS NOT working. could anyone please help me?  local _filter = &#x27;http.requ...'''
date = "2014-12-18T03:54:00Z"
lastmod = "2014-12-18T03:54:00Z"
weight = 38618
keywords = [ "lua", "wireshark" ]
aliases = [ "/questions/38618" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua script to write the source address to text file when wireshark finds a keyword on live capture not working](/questions/38618/lua-script-to-write-the-source-address-to-text-file-when-wireshark-finds-a-keyword-on-live-capture-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38618-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am new to wireshark, tshark and lua.</p><p>try to capture all uri which contains "abc" to text file automatically. the following code does work and i can hear beep when tshark find a filtered uri.</p><p>BUT, writing to text file part IS NOT working.</p><p>could anyone please help me?</p><pre><code>local _filter = &#39;http.request.uri contains &quot;abc&quot;&#39; 
local file = io.open(&quot;Test.txt&quot;, &quot;w&quot;)

local function make_tap(filter)
    local tap = Listener.new(nil, filter)

    function tap.packet()
        for i=1,3 do print &#39;\007&#39; end                       file:write(&quot;Testing....&quot;)       
    end

    return tap   end</code></pre><p>Thanks</p></div><div id="question-tags" class="tags-container tags">lua wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Dec '14, 03:54</strong></p><img src="https://secure.gravatar.com/avatar/fffb59505884915bcdac690c14a93078?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shark&#39;s gravatar image" /><p>Shark<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shark has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Dec '14, 14:46</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-38618" class="comments-container"><span id="38675"></span><div id="comment-38675" class="comment"><div id="post-38675-score" class="comment-score"></div><div class="comment-text"><p>It works for me. Or at least, in my script I use:</p><pre><code>...
local file = io.open(&quot;Test.txt&quot;, &quot;w&quot;)
function myproto.dissector(tvb, pinfo, tree)
    file:write(&quot;Packet: &quot; .. pinfo.number .. &quot;\n&quot;)
end
...</code></pre><p>and it does write out to the file, both using tshark and wireshark.</p></div><div id="comment-38675-info" class="comment-info"><span class="comment-age">(23 Dec '14, 00:59)</span> Hadriel</div></div></div><div id="comment-tools-38618" class="comment-tools"></div><div class="clear"></div><div id="comment-38618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

