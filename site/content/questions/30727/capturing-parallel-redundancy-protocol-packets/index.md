+++
type = "question"
title = "Capturing Parallel redundancy protocol packets"
description = '''Hi, Am trying to make wireshark capture and display prp (parallel redundancy protocol) packets that are being sent by my test board to a pc on which the wire shark is installed. Unfortunately, am not seeing any of the prp frames captured. Am pretty sure that the my test board is sending the prp pack...'''
date = "2014-03-12T05:59:00Z"
lastmod = "2014-03-17T04:03:00Z"
weight = 30727
keywords = [ "prp" ]
aliases = [ "/questions/30727" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing Parallel redundancy protocol packets](/questions/30727/capturing-parallel-redundancy-protocol-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30727-score" class="post-score" title="current number of votes">0</div><span id="post-30727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Am trying to make wireshark capture and display prp (parallel redundancy protocol) packets that are being sent by my test board to a pc on which the wire shark is installed. Unfortunately, am not seeing any of the prp frames captured. Am pretty sure that the my test board is sending the prp packets because i have used ixia to test that. Is there something in the settings that i need to turn on specially for the prp packets? Am able to make my wire shark capture and display normal ethernet packets. I have also tried enabling the PRP field under the Enabled Protocols option (in Analyze tab). But i guess this does not matter for capturing the PRP packets.</p><p>We are using wire shark version 1.10.2</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-prp" rel="tag" title="see questions tagged &#39;prp&#39;">prp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '14, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/e7d566c97adbee1a09ad4458551f4e13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hafiz219&#39;s gravatar image" /><p><span>Hafiz219</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hafiz219 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Mar '14, 06:23</strong> </span></p></div></div><div id="comments-container-30727" class="comments-container"></div><div id="comment-tools-30727" class="comment-tools"></div><div class="clear"></div><div id="comment-30727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30736"></span>

<div id="answer-container-30736" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30736-score" class="post-score" title="current number of votes">1</div><span id="post-30736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I believe PRP is one of those (rare?) dissectors that's disabled by default. Go to <code>Edit-&gt;Preferences-&gt;Protocols-&gt;PRP</code> and check the <code>Enable Dissector</code> flag.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '14, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30736" class="comments-container"><span id="30796"></span><div id="comment-30796" class="comment"><div id="post-30796-score" class="comment-score"></div><div class="comment-text"><p>I tried enabling the prp packet dissector but i dont see wireshark capturing prp frames. I am not sure whether we need a dissector for prp because it is just any packet with a special trailer. It should at least have been shown as a normal packet in wireshark.</p></div><div id="comment-30796-info" class="comment-info"><span class="comment-age">(14 Mar '14, 02:06)</span> <span class="comment-user userinfo">Hafiz219</span></div></div><span id="30797"></span><div id="comment-30797" class="comment"><div id="post-30797-score" class="comment-score"></div><div class="comment-text"><p>How and where did you try to capture the PRP traffic?</p></div><div id="comment-30797-info" class="comment-info"><span class="comment-age">(14 Mar '14, 02:51)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="30802"></span><div id="comment-30802" class="comment"><div id="post-30802-score" class="comment-score"></div><div class="comment-text"><p><span>@Hafiz219</span>: just to be clear, you enabled it by going to the menu <code>Edit-&gt;Preferences-&gt;Protocols-&gt;PRP</code> and checking the box there, yes? Note this is <em>not</em> the same as the <code>Analyze-&gt;Enabled Protocols</code> checkbox (or at least I don't think it is). Your original posted question said you did it through <code>Analyze-&gt;Enabled Protocols</code> but I meant <code>Edit-&gt;Preferences-&gt;Protocols-&gt;PRP</code>.</p></div><div id="comment-30802-info" class="comment-info"><span class="comment-age">(14 Mar '14, 07:52)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="30877"></span><div id="comment-30877" class="comment"><div id="post-30877-score" class="comment-score"></div><div class="comment-text"><p>We changed our test setup now. We are now connecting the ixia to the machine on which Wire shark is installed. The prp packets pumped from the ixia is collected properly by the Wire shark. We didn't even have to change any of the settings i.e we haven't changed any of these 1) Edit -&gt; Preferences -&gt; PRP or 2) Analyze -&gt; Enabled Protocols -&gt; PRP.</p><p>Need to figure out what is wrong when the board is connected. Thanks all, for the comments</p></div><div id="comment-30877-info" class="comment-info"><span class="comment-age">(17 Mar '14, 04:03)</span> <span class="comment-user userinfo">Hafiz219</span></div></div></div><div id="comment-tools-30736" class="comment-tools"></div><div class="clear"></div><div id="comment-30736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

