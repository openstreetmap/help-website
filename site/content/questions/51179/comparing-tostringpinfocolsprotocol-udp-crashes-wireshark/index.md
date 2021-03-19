+++
type = "question"
title = "Comparing tostring(pinfo.cols.protocol) == &#x27;udp&#x27; crashes Wireshark"
description = '''In my custom dissector i&#x27;m having the problem that my dissector isbeing executed on ICMP packages aswell as UDP. In ICMP packages the data is incomplete so the lua script crashes. To avoid running it on ICMP packages I tried comparing the current protocol to UDP but that crashes Wireshark. I&#x27;m not s...'''
date = "2016-03-25T06:04:00Z"
lastmod = "2016-05-03T14:52:00Z"
weight = 51179
keywords = [ "lua", "heur-dissect", "dissection" ]
aliases = [ "/questions/51179" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Comparing tostring(pinfo.cols.protocol) == 'udp' crashes Wireshark](/questions/51179/comparing-tostringpinfocolsprotocol-udp-crashes-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51179-score" class="post-score" title="current number of votes">0</div><span id="post-51179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In my custom dissector i'm having the problem that my dissector isbeing executed on ICMP packages aswell as UDP. In ICMP packages the data is incomplete so the lua script crashes.</p><p>To avoid running it on ICMP packages I tried comparing the current protocol to UDP but that crashes Wireshark.</p><p>I'm not sure if that is the best way of doing it so I'm open to any other suggestion</p><pre><code>function setDefault (t, d)
    local mt = {__index = function () return d end}
    setmetatable(t, mt)
end

do

    local protocols = {
        [0] = &quot;RED&quot;
    }

    local directions = {
        [0] = &quot;Rx&quot;,
        [1] = &quot;Tx&quot;,
        [2] = &quot;RxTx&quot;
    }

    setDefault(protocols, &quot;UNDEFINED&quot;)
    setDefault(directions, &quot;UNKNOWN&quot;)
    local version = &quot;&quot; -- use this when debugging to increase the number of the parser

    -- declare our protocol
    local gsg_proto = Proto(&quot;GSG&quot;..version, &quot;GSG&quot;..version)

    -- create a function to dissect it
    function gsg_proto.dissector(buffer, pinfo, tree)
        message(&quot;protocol &gt;&quot;..tostring(pinfo.cols.protocol)..&quot;&lt;&quot;) -- this works fine
        if tostring(pinfo.cols.protocol) == &#39;udp&#39; then
            pinfo.cols.protocol = &quot;myproto&quot;
            return true
        end
    end

    gsg_proto:register_heuristic(&#39;udp&#39;, gsg_proto.dissector)
end</code></pre><p>Wireshark Version 2.0.2 (v2.0.2-0-ga16e22e from master-2.0) Windows 7</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-heur-dissect" rel="tag" title="see questions tagged &#39;heur-dissect&#39;">heur-dissect</span> <span class="post-tag tag-link-dissection" rel="tag" title="see questions tagged &#39;dissection&#39;">dissection</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '16, 06:04</strong></p><img src="https://secure.gravatar.com/avatar/afd48bc232932c104899bd65f1394ed5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RedX2501&#39;s gravatar image" /><p><span>RedX2501</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RedX2501 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Mar '16, 00:39</strong> </span></p></div></div><div id="comments-container-51179" class="comments-container"></div><div id="comment-tools-51179" class="comment-tools"></div><div class="clear"></div><div id="comment-51179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="51212"></span>

<div id="answer-container-51212" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51212-score" class="post-score" title="current number of votes">0</div><span id="post-51212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It should not be possible to cause Wireshark itself to crash merely by using a Lua script, so this is a bug. Please file a bug on this on <a href="http://buts.wireshark.org">the Wireshark Bugzilla</a>; please attach your Lua script to the bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '16, 15:00</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-51212" class="comments-container"><span id="51215"></span><div id="comment-51215" class="comment"><div id="post-51215-score" class="comment-score"></div><div class="comment-text"><p>Are you able to reproduce this? If so would you mind filling the bug? I don't want to create another account for this....</p></div><div id="comment-51215-info" class="comment-info"><span class="comment-age">(26 Mar '16, 00:37)</span> <span class="comment-user userinfo">RedX2501</span></div></div></div><div id="comment-tools-51212" class="comment-tools"></div><div class="clear"></div><div id="comment-51212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52200"></span>

<div id="answer-container-52200" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52200-score" class="post-score" title="current number of votes">0</div><span id="post-52200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not good with Lua, but the C equivalent to what you want is: pinfo-&gt;ptype == PT_UDP</p><p>So it should be something like: pinfo.port_type == 3 (not sure if PT_ enumeration is accessible in Lua)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '16, 14:52</strong></p><img src="https://secure.gravatar.com/avatar/84070f0cd61650ab31aad30384b959f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael%20Mann&#39;s gravatar image" /><p><span>Michael Mann</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael Mann has no accepted answers">0%</span></p></div></div><div id="comments-container-52200" class="comments-container"></div><div id="comment-tools-52200" class="comment-tools"></div><div class="clear"></div><div id="comment-52200-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

