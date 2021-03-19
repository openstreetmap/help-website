+++
type = "question"
title = "VoIP Roaming Call"
description = '''Roaming calls and RTP path minimization. The issue is that roaming calls are separated into different parts in Wireshark looking like multiple calls instead of a single call. Here is my comment to a person more knowledgable than myself, with their follow up answer. My question is &quot;why can&#x27;t Wireshar...'''
date = "2012-12-13T05:32:00Z"
lastmod = "2012-12-14T05:00:00Z"
weight = 16835
keywords = [ "mobile", "minimization", "roaming", "rtp", "voip" ]
aliases = [ "/questions/16835" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [VoIP Roaming Call](/questions/16835/voip-roaming-call)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16835-score" class="post-score" title="current number of votes">0</div><span id="post-16835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Roaming calls and RTP path minimization. The issue is that roaming calls are separated into different parts in Wireshark looking like multiple calls instead of a single call. Here is my comment to a person more knowledgable than myself, with their follow up answer. My question is "why can't Wireshark understand that this is one phone call (roaming mobile call) and display it as a single call?".</p><p>My original Question related to a single call flow. "The attached call flow ladder diagram (time sequence identical to original pcap). Note the relative intermixed left column 1s and 0s. If this were truly one call in a roaming scenario, or some other sequential exchange during the same call, wouldn’t it be more evenly divided (mostly 0s at the top and mostly 1s at the bottom)? This was really apparent in Wireshark because it color codes the two separate calls when you select both before generating the flow diagram. This looks more like two separate calls just intermixed in time as they both arrive essentially in parallel."</p><p>Answer: "This is exactly what a roaming scenario looks like. A calls B (A’s MSC sends B’s home MSC an INVITE). MSC B determines that mobile B is roaming in MSC C. (this is done with IS-41 signaling, MSC C sends MSC B a TLDN). MSC B sends an INVITE to MSC C using the TLDN so that MSC C knows the call is for mobile B. MSC C alerts mobile B. When mobile B answers, the 200 OK INVITE goes from MSC C to MSC B then from MSC B to MSC A. At that time path minimization happens. MSC B sends and empty re-invite to MSC C. When MSC C responds with its SDP, MSC B sends a re-INVITE to MSC A containing C’s SDP. When MSC A responds with SDP, MSC B sends A’s SDP to C. This allows MSC A and MSC C to exchange RTP directly. This also can happen with Call Forwarding Immediate. For Call Forwarding No Answer (to voice mail for example), you will see A to B set up then, later B to C set up. When answer occurs, path minimization will also occur, but CFNA will look a bit different since the two legs were set up in series instead of parallel. If these were independent calls, you would not see the same SDP RTP IP/port passed from one dialog to the another. That is a sign of path minimization."</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mobile" rel="tag" title="see questions tagged &#39;mobile&#39;">mobile</span> <span class="post-tag tag-link-minimization" rel="tag" title="see questions tagged &#39;minimization&#39;">minimization</span> <span class="post-tag tag-link-roaming" rel="tag" title="see questions tagged &#39;roaming&#39;">roaming</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '12, 05:32</strong></p><img src="https://secure.gravatar.com/avatar/494c8789f937dede544fbd1fe319e075?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomEverett&#39;s gravatar image" /><p><span>TomEverett</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomEverett has no accepted answers">0%</span></p></div></div><div id="comments-container-16835" class="comments-container"></div><div id="comment-tools-16835" class="comment-tools"></div><div class="clear"></div><div id="comment-16835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16838"></span>

<div id="answer-container-16838" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16838-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16838-score" class="post-score" title="current number of votes">0</div><span id="post-16838-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The question is "Why should it?". This tool is just for that purpose, showing you the raw and dirty details of the sessions making up the "call". You'll want to see all the transactions between the nodes involved, especially when something is not working as expected.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '12, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-16838" class="comments-container"><span id="16840"></span><div id="comment-16840" class="comment"><div id="post-16840-score" class="comment-score"></div><div class="comment-text"><p>I am completely baffled by your comment. No detail is lost if all you want to do is know the association between calls. Currently if two calls are part of the same roaming call which make up the complete call flow then "complete" is ambiguous and misleading. Having some idea of calls associated with the same logical phone conversation is beneficial.</p></div><div id="comment-16840-info" class="comment-info"><span class="comment-age">(13 Dec '12, 08:12)</span> <span class="comment-user userinfo">TomEverett</span></div></div><span id="16841"></span><div id="comment-16841" class="comment"><div id="post-16841-score" class="comment-score"></div><div class="comment-text"><p>Also for the process of extracting and replaying call scenarios, not knowing which parts of the call are related makes it more difficult to identify what needs to be extracted. In my world, live captures result in giga byte files with MANY intermixed calls that are difficult enough to analyze. All I am asking is if there is some way to simplify analysis of these types of call flows.</p></div><div id="comment-16841-info" class="comment-info"><span class="comment-age">(13 Dec '12, 08:12)</span> <span class="comment-user userinfo">TomEverett</span></div></div><span id="16842"></span><div id="comment-16842" class="comment"><div id="post-16842-score" class="comment-score"></div><div class="comment-text"><p>Digg into the code and maske it better?</p></div><div id="comment-16842-info" class="comment-info"><span class="comment-age">(13 Dec '12, 08:30)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="16865"></span><div id="comment-16865" class="comment"><div id="post-16865-score" class="comment-score"></div><div class="comment-text"><p><span>@TomEverett</span>: It's very simple to ask, but if you've ever dealt with multivendor UC/US combinations, the multitude of RFC's (try figuring out the many ways to do call transfer) involved with SIP, the (sometimes) errant operations of B2B UAs, etc, you'll know this is a (very) tall order. Then multiply that by all the other call control protocols supported by Wireshark and the task becomes immense.</p><p>This then can be seen as outside the scope of what Wireshark is intended for. What you seek is a SIP Session Analyzer, but the few I found even don't do what you want.</p></div><div id="comment-16865-info" class="comment-info"><span class="comment-age">(14 Dec '12, 04:20)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="16869"></span><div id="comment-16869" class="comment"><div id="post-16869-score" class="comment-score"></div><div class="comment-text"><p>"multivendor UC/US combinations, the multitude of RFC's, the (sometimes) errant operations of B2B UAs, etc"</p><p>I live in this world that is why I posted the question. If you feel my comment or request is outside the scope of Wireshark just say so. Just don't assume that I don't know what I am talking about.<br />
I have looked at and used many SIP analyzers, some even very expensive, and all have their own strengths and weaknesses. As you very accurately pointed out "the few I found even don't do what you want" this is a problem that needs a solution. The very definition of engineering. Wireshark is a very useful tool. It could be better, or it could spin off into other more focused tools for things like SIP. Either way this added functionality would be a good thing.<br />
This will be my last post on this issue.</p></div><div id="comment-16869-info" class="comment-info"><span class="comment-age">(14 Dec '12, 05:00)</span> <span class="comment-user userinfo">TomEverett</span></div></div></div><div id="comment-tools-16838" class="comment-tools"></div><div class="clear"></div><div id="comment-16838-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

