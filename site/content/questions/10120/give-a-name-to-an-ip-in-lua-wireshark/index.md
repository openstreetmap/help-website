+++
type = "question"
title = "Give a name to an ip in lua wireshark"
description = '''Hi,  how can i give a name to an ip address of a tcp packet in lua? (I want to see in wireshark a name instead of the ip address). Thanks. '''
date = "2012-04-13T02:34:00Z"
lastmod = "2012-04-13T08:44:00Z"
weight = 10120
keywords = [ "lua", "dissector", "wireshark" ]
aliases = [ "/questions/10120" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Give a name to an ip in lua wireshark](/questions/10120/give-a-name-to-an-ip-in-lua-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10120-score" class="post-score" title="current number of votes">0</div><span id="post-10120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>how can i give a name to an ip address of a tcp packet in lua?</p><p>(I want to see in wireshark a name instead of the ip address).</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '12, 02:34</strong></p><img src="https://secure.gravatar.com/avatar/1f3e4aeb3a40e8efc02ddde263388b99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zvika&#39;s gravatar image" /><p><span>Zvika</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zvika has no accepted answers">0%</span></p></div></div><div id="comments-container-10120" class="comments-container"></div><div id="comment-tools-10120" class="comment-tools"></div><div class="clear"></div><div id="comment-10120-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10130"></span>

<div id="answer-container-10130" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10130-score" class="post-score" title="current number of votes">0</div><span id="post-10130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Name resolution and Lua are independent of each other; and Wireshark Lua has no built-in API to control name resolution, but you can do it with the following instructions (untested).</p><ol><li><p>Make sure name resolution is enabled in preferences: <strong>Preferences &gt; Name Resolution &gt; Enable network name resolution</strong></p></li><li><p>Creates a <code>hosts</code> file at:</p><ul><li><code>%APPDATA%\\Wireshark\\hosts</code> <strong>(Windows)</strong></li><li><code>~/.wireshark/hosts</code> <strong>(*nix)</strong></li></ul></li><li><p>For each custom name, add an entry to the <code>hosts</code> file on a new line in the form of:</p><p><em>{ipaddress} {name}</em></p></li></ol><p>Ex: This <code>hosts</code> file has 3 custom name resolutions:</p><pre><code>192.168.1.1 wifi_router
192.168.1.2 wifi_clientA
192.168.1.3 wifi_clientB</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '12, 08:44</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p><span>bstn</span><br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Apr '12, 08:45</strong> </span></p></div></div><div id="comments-container-10130" class="comments-container"></div><div id="comment-tools-10130" class="comment-tools"></div><div class="clear"></div><div id="comment-10130-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

