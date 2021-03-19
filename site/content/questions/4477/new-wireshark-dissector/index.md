+++
type = "question"
title = "new wireshark dissector"
description = '''Hi,  I am developing a new wireshark dissector. I have a pcap file the could be opened from wireshark how do I get my plugin to read this file. If I feed it through a port I can write the port to my dissector code to listen in that port. How does a plugin get activated when a pcap file is opened??? ...'''
date = "2011-06-09T13:01:00Z"
lastmod = "2011-06-09T20:02:00Z"
weight = 4477
keywords = [ "dissector", "plugin" ]
aliases = [ "/questions/4477" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [new wireshark dissector](/questions/4477/new-wireshark-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4477-score" class="post-score" title="current number of votes">0</div><span id="post-4477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am developing a new wireshark dissector. I have a pcap file the could be opened from wireshark how do I get my plugin to read this file. If I feed it through a port I can write the port to my dissector code to listen in that port. How does a plugin get activated when a pcap file is opened???</p><p>Thanks in Advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '11, 13:01</strong></p><img src="https://secure.gravatar.com/avatar/25b19db92f6c5c1102813db491e41432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tut087&#39;s gravatar image" /><p><span>tut087</span><br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tut087 has no accepted answers">0%</span></p></div></div><div id="comments-container-4477" class="comments-container"><span id="4487"></span><div id="comment-4487" class="comment"><div id="post-4487-score" class="comment-score"></div><div class="comment-text"><p>Dissectors don't read capture files; the core of Wireshark reads capture files, and calls the dissector for the link-layer header type for the packet, which then calls other dissectors.</p><p>Your dissector presumably dissects packets for a particular protocol; does that protocol run at the link layer, or does it run atop another protocol?</p></div><div id="comment-4487-info" class="comment-info"><span class="comment-age">(09 Jun '11, 20:02)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-4477" class="comment-tools"></div><div class="clear"></div><div id="comment-4477-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4485"></span>

<div id="answer-container-4485" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4485-score" class="post-score" title="current number of votes">2</div><span id="post-4485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you're having trouble integrating your plugin with Wireshark, then try reading <a href="http://anonsvn.wireshark.org/wireshark/trunk/doc/README.developer">README.developer</a> and <a href="http://anonsvn.wireshark.org/wireshark/trunk/doc/README.plugins">README.plugins</a> in particular.</p><p>If your plugin is already compiled and integrated but it's just not getting handed packets that you think it should be handed, then you probably need to register your plugin on whichever UDP or TCP port your traffic is appearing on.</p><p>If the port can vary, then you might consider adding a port preference to your dissector so it's configurable. Alternatively, if the port could change frequently and it's too annoying to have to keep changing the port preference, you could try registering your plugin as a heuristic dissector instead. Refer to <a href="http://anonsvn.wireshark.org/wireshark/trunk/doc/README.heuristic">README.heuristic</a> in that case.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '11, 15:49</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Jun '11, 16:05</strong> </span></p></div></div><div id="comments-container-4485" class="comments-container"></div><div id="comment-tools-4485" class="comment-tools"></div><div class="clear"></div><div id="comment-4485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

