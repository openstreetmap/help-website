+++
type = "question"
title = "decode as feature set up before start a cap"
description = '''Hi all, is it possible to set up a capture filter in wireshark for the decode as feature just like tshark -d option i.e. -d udp.port==8000,rudp, before to start capture ?'''
date = "2011-04-08T06:59:00Z"
lastmod = "2011-04-11T09:01:00Z"
weight = 3406
keywords = [ "decode", "capture-filter" ]
aliases = [ "/questions/3406" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [decode as feature set up before start a cap](/questions/3406/decode-as-feature-set-up-before-start-a-cap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3406-score" class="post-score" title="current number of votes">0</div><span id="post-3406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, is it possible to set up a capture filter in wireshark for the decode as feature just like tshark -d option i.e. -d udp.port==8000,rudp, before to start capture ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '11, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/f39dfb2756b60f90a417b0e33c0201b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flap78&#39;s gravatar image" /><p><span>flap78</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flap78 has no accepted answers">0%</span></p></div></div><div id="comments-container-3406" class="comments-container"></div><div id="comment-tools-3406" class="comment-tools"></div><div class="clear"></div><div id="comment-3406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3441"></span>

<div id="answer-container-3441" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3441-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3441-score" class="post-score" title="current number of votes">1</div><span id="post-3441-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could do that using lua</p><p>In your c:program filesWireshark directory find init.lua file.</p><p>Comment out disable_lua line and at the end of the file add dofile("decodes.lua"). Then create a file in the same directory called decodes.lua</p><p>Edit it to have contents like below</p><pre><code>do
    local rudp_dissector=Dissector.get(&quot;rudp&quot;)
    local udp_table=DissectorTable.get(&quot;udp.port&quot;)
    udp_table:add(8000, rudp_dissector)
end</code></pre><p>Now each time you start wireshark traffic on 8000 port will be decoded as rudp</p><p>Instead of having it as permanent solution you can use command line option <strong>-Xlua_script:./decodes.lua</strong> when starting wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '11, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p><span>izopizo</span><br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-3441" class="comments-container"></div><div id="comment-tools-3441" class="comment-tools"></div><div class="clear"></div><div id="comment-3441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3440"></span>

<div id="answer-container-3440" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3440-score" class="post-score" title="current number of votes">0</div><span id="post-3440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Currently this is not possible, but there has been interest in having this feature available. See bugs <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2931">2931</a> and <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5143">5143</a> in particular. Perhaps someone will implement this one day.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '11, 07:49</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3440" class="comments-container"></div><div id="comment-tools-3440" class="comment-tools"></div><div class="clear"></div><div id="comment-3440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

