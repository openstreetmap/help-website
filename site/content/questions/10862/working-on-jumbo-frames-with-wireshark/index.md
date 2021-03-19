+++
type = "question"
title = "Working on jumbo frames with Wireshark"
description = '''I was asked to do a pcap for an applicaiton that is using jumbo frames over a fiber connection. Are there any special settings - or trap doors - that I need to be aware of? All my captures up to date have been with MTU 1500 and down. Thanks '''
date = "2012-05-09T20:30:00Z"
lastmod = "2012-05-16T19:44:00Z"
weight = 10862
keywords = [ "jumboframes" ]
aliases = [ "/questions/10862" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Working on jumbo frames with Wireshark](/questions/10862/working-on-jumbo-frames-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10862-score" class="post-score" title="current number of votes">0</div><span id="post-10862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was asked to do a pcap for an applicaiton that is using jumbo frames over a fiber connection. Are there any special settings - or trap doors - that I need to be aware of? All my captures up to date have been with MTU 1500 and down.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-jumboframes" rel="tag" title="see questions tagged &#39;jumboframes&#39;">jumboframes</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '12, 20:30</strong></p><img src="https://secure.gravatar.com/avatar/f797bdc41d990dca073837114e048b1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EricKnaus&#39;s gravatar image" /><p><span>EricKnaus</span><br />
<span class="score" title="46 reputation points">46</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EricKnaus has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 May '12, 12:07</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-10862" class="comments-container"></div><div id="comment-tools-10862" class="comment-tools"></div><div class="clear"></div><div id="comment-10862-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10877"></span>

<div id="answer-container-10877" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10877-score" class="post-score" title="current number of votes">0</div><span id="post-10877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="EricKnaus has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think there will be any trap doors, Wireshark should be able to handle jumbo frames just fine. If I were you I'd just do a capture and see what I get :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '12, 01:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-10877" class="comments-container"><span id="10879"></span><div id="comment-10879" class="comment"><div id="post-10879-score" class="comment-score"></div><div class="comment-text"><p>According to a recent <a href="http://ask.wireshark.org/questions/9542/wireshark-and-jumbograms">post</a>, Wireshark can't handle jumbograms above 64kB.</p></div><div id="comment-10879-info" class="comment-info"><span class="comment-age">(10 May '12, 02:00)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="10881"></span><div id="comment-10881" class="comment"><div id="post-10881-score" class="comment-score"></div><div class="comment-text"><p>Just a second, we're talking jumbo <strong>frames</strong> not jumbo<strong>grams</strong>. The first are "oversized" ethernet frames with an MTU of 9000, while jumbograms are IPv6 specific packets that can be much larger than 64k. I doubt EricKnaus was asking about those - as far as I read it he really meant run-of-the-mill ethernet jumbo frames.</p></div><div id="comment-10881-info" class="comment-info"><span class="comment-age">(10 May '12, 02:04)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="10883"></span><div id="comment-10883" class="comment"><div id="post-10883-score" class="comment-score"></div><div class="comment-text"><p>Ok, I see. I'm no expert at "jumbo-anything" ...but I'm pretty good at skimming posts ;)</p><p>The question is titled "jumbo frames", the body indicates "jumbo packets", and it's tagged as "jumbograms". I don't know what the target is.</p></div><div id="comment-10883-info" class="comment-info"><span class="comment-age">(10 May '12, 02:08)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="10884"></span><div id="comment-10884" class="comment"><div id="post-10884-score" class="comment-score"></div><div class="comment-text"><p>True, the wording is a bit inconsistent in the question. But I think we can rule out IPv6 jumbograms at the moment since I doubt anyone is using them for anything beyond some kind of IPv6 lab experiments :-)</p></div><div id="comment-10884-info" class="comment-info"><span class="comment-age">(10 May '12, 02:12)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="10886"></span><div id="comment-10886" class="comment"><div id="post-10886-score" class="comment-score"></div><div class="comment-text"><p>I see only one "trap door". There are switches which allow configuration of jumbo frames:</p><ul><li>system wide</li><li>on a vlan</li><li>on a port</li></ul><p>So, just ensure, you enabled jumbo frames on your mirroring/monitoring port, otherwise you might not see some frames. Please consult your switch manual.</p></div><div id="comment-10886-info" class="comment-info"><span class="comment-age">(10 May '12, 02:16)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="10897"></span><div id="comment-10897" class="comment not_top_scorer"><div id="post-10897-score" class="comment-score"></div><div class="comment-text"><p>Yes, I was not specific - it's jumbo frames. Kurt's comments helps too. Btw, in what sort of environment would I run into jumbograms? and then how would I capture/read them? I see IPv6 all over the place in many PCAP's but have not paid that much attention to them as they usually constitute less than 6% of the traffic and are usually router or W7 machines that use a v4 address anyway.</p></div><div id="comment-10897-info" class="comment-info"><span class="comment-age">(10 May '12, 07:27)</span> <span class="comment-user userinfo">EricKnaus</span></div></div><span id="10899"></span><div id="comment-10899" class="comment not_top_scorer"><div id="post-10899-score" class="comment-score"></div><div class="comment-text"><p>At the moment I doubt you'll see Jumbograms anywhere except in some mad scientists laboratories where they're fiddling around with the jumbogram option that IPv6 has :-) The problem is that there is still the ethernet MTU at 1500 or 9000 bytes, so unless you're running Jumbograms on a different medium with larger frame sizes you'll have to fragment them. And that is not really efficient, so I doubt we'll see much use of Jumbograms anytime soon.</p></div><div id="comment-10899-info" class="comment-info"><span class="comment-age">(10 May '12, 07:48)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="11075"></span><div id="comment-11075" class="comment not_top_scorer"><div id="post-11075-score" class="comment-score"></div><div class="comment-text"><p>Well, there actually was 1 trap door. The laptops we were using would not see anything over 1500MTU! We were able to ping to the servers with jumbo frames and see them that way but were were hoping to do this "in line". The setting that we played with on our servers but not on the units we were trying to capture with (W7, 64bit, 10/100/1000) - 2 year old Dells. Can I use this as an excuse to get something new and cool when I explain this to my wife? ... er for work ofcourse!</p></div><div id="comment-11075-info" class="comment-info"><span class="comment-age">(16 May '12, 19:44)</span> <span class="comment-user userinfo">EricKnaus</span></div></div></div><div id="comment-tools-10877" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-10877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

