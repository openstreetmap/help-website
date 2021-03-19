+++
type = "question"
title = "How can I follow a particular TCP stream if a packet belongs to more than one stream?"
description = '''I have write a wireshark dissector to analyse my onw protocol whitch are more than one TCP headers in a packet, how can I check the tcp seq stream of innter tcp or outter tcp. the packet look like the follow: [mac|outter ip|outter tcp|myprotocal header|inner ip|inner tcp|appdate]'''
date = "2016-09-18T22:59:00Z"
lastmod = "2016-09-21T00:36:00Z"
weight = 55640
keywords = [ "dissector", "tcp.stream" ]
aliases = [ "/questions/55640" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I follow a particular TCP stream if a packet belongs to more than one stream?](/questions/55640/how-can-i-follow-a-particular-tcp-stream-if-a-packet-belongs-to-more-than-one-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55640-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55640-score" class="post-score" title="current number of votes">0</div><span id="post-55640-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have write a wireshark dissector to analyse my onw protocol whitch are more than one TCP headers in a packet, how can I check the tcp seq stream of innter tcp or outter tcp.</p><p>the packet look like the follow: [mac|outter ip|outter tcp|myprotocal header|inner ip|inner tcp|appdate]</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tcp.stream" rel="tag" title="see questions tagged &#39;tcp.stream&#39;">tcp.stream</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '16, 22:59</strong></p><img src="https://secure.gravatar.com/avatar/06873e10edc62e4ff547a6e2c5ef5e25?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmqy&#39;s gravatar image" /><p><span>cmqy</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmqy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Sep '16, 19:19</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-55640" class="comments-container"></div><div id="comment-tools-55640" class="comment-tools"></div><div class="clear"></div><div id="comment-55640-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55672"></span>

<div id="answer-container-55672" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55672-score" class="post-score" title="current number of votes">0</div><span id="post-55672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Currently, you can't; the comment in the code that produces the message you reported says</p><pre><code>/* XXX fix this later, we should show a dialog allowing the user
   to select which session he wants here
*/</code></pre><p>but that hasn't been fixed yet. You might want to file a request for enhancement on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a> to make it easier to track changes for this, including any fix.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '16, 19:20</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-55672" class="comments-container"><span id="55691"></span><div id="comment-55691" class="comment"><div id="post-55691-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much!</p></div><div id="comment-55691-info" class="comment-info"><span class="comment-age">(21 Sep '16, 00:36)</span> <span class="comment-user userinfo">cmqy</span></div></div></div><div id="comment-tools-55672" class="comment-tools"></div><div class="clear"></div><div id="comment-55672-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

