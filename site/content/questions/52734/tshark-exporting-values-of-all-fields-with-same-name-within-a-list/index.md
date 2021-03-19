+++
type = "question"
title = "Tshark - Exporting values of all fields with same name within a list"
description = '''With reference to the below S1AP pcap log snapshot  The highlighted field above is s1ap.iE_Extensions which contains a list of items. I need to use Tshark to extract the id: field (s1ap.id) from Item0 and Item1 along with some other fields. My tshark command looks like below as of now -  tshark -r t...'''
date = "2016-05-18T07:56:00Z"
lastmod = "2016-05-18T08:15:00Z"
weight = 52734
keywords = [ "tshark" ]
aliases = [ "/questions/52734" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark - Exporting values of all fields with same name within a list](/questions/52734/tshark-exporting-values-of-all-fields-with-same-name-within-a-list)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52734-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52734-score" class="post-score" title="current number of votes">0</div><span id="post-52734-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>With reference to the below S1AP pcap log snapshot</p><p><a href="http://i.stack.imgur.com/2nh9m.png"><img src="http://i.stack.imgur.com/2nh9m.png" alt="enter image description here" /></a></p><p>The highlighted field above is <code>s1ap.iE_Extensions</code> which contains a list of items. I need to use Tshark to extract the <code>id:</code> field (<code>s1ap.id</code>) from <code>Item0</code> and <code>Item1</code> along with some other fields.</p><p>My tshark command looks like below as of now -</p><p><code>tshark -r test.pcap -Y "s1ap.procedureCode == 9" -T fields -e frame.time  -e s1ap.procedureCode -E header=y -E separator=, &gt; pcap_to_csv.csv</code></p><ul><li>need help with exapanding the command so as to get the above fields (<code>s1ap.id</code>) for each item in <code>s1ap.iE_Extensions</code> list included in the exported file</li></ul></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '16, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/d1d9561850217ca49173676d29d4632d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wire990099&#39;s gravatar image" /><p><span>wire990099</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wire990099 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-52734" class="comments-container"></div><div id="comment-tools-52734" class="comment-tools"></div><div class="clear"></div><div id="comment-52734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52737"></span>

<div id="answer-container-52737" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52737-score" class="post-score" title="current number of votes">1</div><span id="post-52737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Just add the <code>-e s1ap.id</code> once, you should get a list of all these fields found in the frame. "Should" because I do that with <code>usb.iso.data</code> which exists multiple times in a frame, but I don't output anything else so I cannot say how the values of <code>s1ap.id</code> will be arranged among the values of the other fields and separated from each other.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 May '16, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-52737" class="comments-container"></div><div id="comment-tools-52737" class="comment-tools"></div><div class="clear"></div><div id="comment-52737-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

