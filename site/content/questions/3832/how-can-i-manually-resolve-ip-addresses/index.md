+++
type = "question"
title = "How can I manually resolve IP addresses?"
description = '''Here in front of m,e I have a reference IMS paper with many IP addresses.  In the .pcap file, a few IP addresses were manually resolved so a trace is a little more &quot;likeable&quot;.  I saved this trace file as a new one, and then opened this newly created file. At first it was ok -IP addresses were still ...'''
date = "2011-04-29T18:09:00Z"
lastmod = "2012-02-24T06:36:00Z"
weight = 3832
keywords = [ "reset", "save", "resolve", "address" ]
aliases = [ "/questions/3832" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I manually resolve IP addresses?](/questions/3832/how-can-i-manually-resolve-ip-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3832-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3832-score" class="post-score" title="current number of votes">0</div><span id="post-3832-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Here in front of m,e I have a reference IMS paper with many IP addresses. In the .pcap file, a few IP addresses were manually resolved so a trace is a little more "likeable". I saved this trace file as a new one, and then opened this newly created file. At first it was ok -IP addresses were still displayed with names (words) -but now, when this new file was opened again, there are IP addresses again.</p><p>What can I do so IP addresses will always be displayed with words?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reset" rel="tag" title="see questions tagged &#39;reset&#39;">reset</span> <span class="post-tag tag-link-save" rel="tag" title="see questions tagged &#39;save&#39;">save</span> <span class="post-tag tag-link-resolve" rel="tag" title="see questions tagged &#39;resolve&#39;">resolve</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '11, 18:09</strong></p><img src="https://secure.gravatar.com/avatar/13231e33ab17a93476f7b98c9d5b272a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wired&#39;s gravatar image" /><p><span>wired</span><br />
<span class="score" title="44 reputation points">44</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wired has one accepted answer">9%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Feb '12, 17:17</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-3832" class="comments-container"><span id="3833"></span><div id="comment-3833" class="comment"><div id="post-3833-score" class="comment-score"></div><div class="comment-text"><p>Well, now it works again...strange. :-s</p></div><div id="comment-3833-info" class="comment-info"><span class="comment-age">(29 Apr '11, 18:31)</span> <span class="comment-user userinfo">wired</span></div></div></div><div id="comment-tools-3832" class="comment-tools"></div><div class="clear"></div><div id="comment-3832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3839"></span>

<div id="answer-container-3839" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3839-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3839-score" class="post-score" title="current number of votes">2</div><span id="post-3839-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wired has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This all depends on how the name resolution engine is fed with information. It can have several sources:</p><ul><li>DNS</li><li>Host file name</li><li>Manual entries</li></ul><p>The only permanent way is to setup a <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChAdvNameResolutionSection.html">hosts file</a> with the capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '11, 02:13</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3839" class="comments-container"><span id="9192"></span><div id="comment-9192" class="comment"><div id="post-9192-score" class="comment-score"></div><div class="comment-text"><p>Update: according to http://ask.wireshark.org/questions/9173/can-i-save-manual-address-resolutions the current development version (1.7.x) does allow you to save such name resolutions into a PCAP-NG file.</p></div><div id="comment-9192-info" class="comment-info"><span class="comment-age">(24 Feb '12, 06:36)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-3839" class="comment-tools"></div><div class="clear"></div><div id="comment-3839-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

