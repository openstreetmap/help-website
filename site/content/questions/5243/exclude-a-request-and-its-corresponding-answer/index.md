+++
type = "question"
title = "Exclude a request and its corresponding answer"
description = '''Hello All, I hope someone can help me out with this issue I am facing. I had a question regarding Wireshark filters. I am trying to filter out packets according to &quot;Subscriber ID&quot;. However this attribute is only present in the &quot;Request&quot; packets. The &quot;Answer&quot; packets correspnding to these requests do...'''
date = "2011-07-26T01:50:00Z"
lastmod = "2011-08-01T00:40:00Z"
weight = 5243
keywords = [ "filter", "mate", "mates", "related" ]
aliases = [ "/questions/5243" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Exclude a request and its corresponding answer](/questions/5243/exclude-a-request-and-its-corresponding-answer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5243-score" class="post-score" title="current number of votes">0</div><span id="post-5243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>I hope someone can help me out with this issue I am facing. I had a question regarding Wireshark filters. I am trying to filter out packets according to "Subscriber ID". However this attribute is only present in the "Request" packets. The "Answer" packets correspnding to these requests do not contain "Subscriber ID" attribute. As a result I end up having the packets of type "Answer". I tried to find a common attribute between the "Request" and "Answer" packets so that I can filter both types (Request and Answer) according to it; however I was not able to.</p><p>My question is the following; is there a way by which I can apply a filter that also removes any related packets? (in that case it is supposed to remove any "Answer" packets)</p><p>I find the way I described the filter I need confusing, in case any clarifications is needed please inform me.</p><p>Thanks a lot for the support !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-mate" rel="tag" title="see questions tagged &#39;mate&#39;">mate</span> <span class="post-tag tag-link-mates" rel="tag" title="see questions tagged &#39;mates&#39;">mates</span> <span class="post-tag tag-link-related" rel="tag" title="see questions tagged &#39;related&#39;">related</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '11, 01:50</strong></p><img src="https://secure.gravatar.com/avatar/883ca3c91538e5ab59c52c9c29f04e00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="walidbaher&#39;s gravatar image" /><p><span>walidbaher</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="walidbaher has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jul '11, 02:02</strong> </span></p></div></div><div id="comments-container-5243" class="comments-container"></div><div id="comment-tools-5243" class="comment-tools"></div><div class="clear"></div><div id="comment-5243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5268"></span>

<div id="answer-container-5268" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5268-score" class="post-score" title="current number of votes">2</div><span id="post-5268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you can find a way to group the answer to the request, you could use <a href="http://wiki.wireshark.org/Mate">MATE</a> to create Groups Of Packets for each subscriber ID and then (I think) filter on/out any GOPs with the Subscriber ID you're interested in.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '11, 10:14</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-5268" class="comments-container"><span id="5337"></span><div id="comment-5337" class="comment"><div id="post-5337-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much for your reply :).</p><p>I read about mate, however I have no idea how to use it :$ I checked a tutorial but was not able to follow it clearly. Namely I have this attribute in all the answer requests that I want to exclude (diameter.cmd.code == 280). I thought I filter out all the answers according to this attribute and then use MATE to get also their corresponding Requests, however I couldn't manage to do so.</p><p>Am I mistaken in the usage of MATE?</p></div><div id="comment-5337-info" class="comment-info"><span class="comment-age">(28 Jul '11, 01:16)</span> <span class="comment-user userinfo">walidbaher</span></div></div><span id="5345"></span><div id="comment-5345" class="comment"><div id="post-5345-score" class="comment-score">1</div><div class="comment-text"><p>[BTW, your last "answer" isn't an answer, so you should probably convert it to a comment.]</p><p>Here's an example MATE file I used to use to detect SCTP retransmissions--back before Wireshark did so on its own:</p><pre><code>Pdu sctp_pdu Proto sctp Transport ip {
        //Extract addr From ip.addr;
        //Extract port From sctp.port;
    Extract vtag From sctp.verification_tag;
    Extract tsn From sctp.data_tsn;
    //Extract sctp_chunk From sctp.chunk_type;
};

Gop sctpretrans On sctp_pdu Match (vtag, tsn) {
    Start();
    Stop(never);
};

Done;</code></pre><p>This creates a GOP when the vtag and tsn match. In this case if I wanted to view everything that is NOT a retransmission, I could filter on "!sctpretrans".</p><p>I believe you could do something similar: first create a GOP of requests+responses (which presumably have something in common) and then filter out that GOP. That would leave you only with requests with no answer and responses with no request (which is what I think you're trying to do).</p></div><div id="comment-5345-info" class="comment-info"><span class="comment-age">(28 Jul '11, 08:31)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="5346"></span><div id="comment-5346" class="comment"><div id="post-5346-score" class="comment-score"></div><div class="comment-text"><p>Oops, sorry, looks like your last answer is a comment--I swear it wasn't a few minutes ago, but maybe I was wrong!</p></div><div id="comment-5346-info" class="comment-info"><span class="comment-age">(28 Jul '11, 08:34)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="5374"></span><div id="comment-5374" class="comment"><div id="post-5374-score" class="comment-score"></div><div class="comment-text"><p>Lol ok no probs, I believe however that I posted my last comment as an answer as I remember clicking "Answer your own question", anyways I am sorry for the confusion but I am still a wireshark/wireshark-ask newbie :D</p><p>Anyways I will read into your suggestions (GOP and so forth) to figure out how I can apply it in my case.</p><p>Thank you so much for your reply :)</p></div><div id="comment-5374-info" class="comment-info"><span class="comment-age">(01 Aug '11, 00:40)</span> <span class="comment-user userinfo">walidbaher</span></div></div></div><div id="comment-tools-5268" class="comment-tools"></div><div class="clear"></div><div id="comment-5268-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5246"></span>

<div id="answer-container-5246" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5246-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5246-score" class="post-score" title="current number of votes">0</div><span id="post-5246-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is a workaround. First of all make a backup of the trace :D. Then list all the "Requests" according to the attribute you are searching for. Then "Edit" -&gt; "Ignore All Displayed Packets". As a result all the "Answers" relating to these packets will be marked with a black color and then you can find out which answers are of importance to you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '11, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/883ca3c91538e5ab59c52c9c29f04e00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="walidbaher&#39;s gravatar image" /><p><span>walidbaher</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="walidbaher has no accepted answers">0%</span></p></div></div><div id="comments-container-5246" class="comments-container"></div><div id="comment-tools-5246" class="comment-tools"></div><div class="clear"></div><div id="comment-5246-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

