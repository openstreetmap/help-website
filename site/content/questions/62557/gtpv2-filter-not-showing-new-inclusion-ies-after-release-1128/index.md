+++
type = "question"
title = "GTPV2 Filter not showing new inclusion IEs after release 1.12.8"
description = '''Hi, I installed wireshark version 2.2.4 in centos6. But not able to view the gtv2 new inclusion IEs after wireshark release 1.12.8 in filter box. Is it display problem or those IEs not registered? Currently I don&#x27;t have pcap files with those IEs.'''
date = "2017-07-06T01:40:00Z"
lastmod = "2017-07-10T06:04:00Z"
weight = 62557
keywords = [ "gtpv2c", "display-filter" ]
aliases = [ "/questions/62557" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [GTPV2 Filter not showing new inclusion IEs after release 1.12.8](/questions/62557/gtpv2-filter-not-showing-new-inclusion-ies-after-release-1128)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62557-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62557-score" class="post-score" title="current number of votes">0</div><span id="post-62557-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I installed wireshark version 2.2.4 in centos6. But not able to view the gtv2 new inclusion IEs after wireshark release 1.12.8 in filter box. Is it display problem or those IEs not registered? Currently I don't have pcap files with those IEs.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gtpv2c" rel="tag" title="see questions tagged &#39;gtpv2c&#39;">gtpv2c</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '17, 01:40</strong></p><img src="https://secure.gravatar.com/avatar/48912e037040264c21d2e543aca485e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abhisek&#39;s gravatar image" /><p><span>Abhisek</span><br />
<span class="score" title="16 reputation points">16</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abhisek has no accepted answers">0%</span></p></div></div><div id="comments-container-62557" class="comments-container"><span id="62558"></span><div id="comment-62558" class="comment"><div id="post-62558-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure what you are asking are you saying that if you list all filters in GTPv2 in Wireshark release 1.12.8 and compare with the list in 2.2.4 you get no difference? If you are looking for specific filters please give example. Possibly the inclusion you are seeking didn't make 2.2.0, no new functionality is added to the branches after release.</p></div><div id="comment-62558-info" class="comment-info"><span class="comment-age">(06 Jul '17, 01:57)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="62561"></span><div id="comment-62561" class="comment"><div id="post-62561-score" class="comment-score"></div><div class="comment-text"><p>Problem is: Some IEs are shown GREEN in FILTERBOX, whereas Some IEs are shown RED in FILTERBOX. ASSUMTION: in FilterBox the IE gtpv2.authentication_quadruplets(introduced after rel-1.12.8) is searched for and it's shown RED not GREEN, whereas gtv2.daf(introduced rel 1.12.8) is shown GREEN. But after some close code walk-through of packet-gtpv2.c, i find that in hf_register_info, one half of IEs are shown properly(GREEN) in FilterBox, whereas the next half is not shown(RED) in FilterBox. So The first assumption is wrong. Now the question-"IS THERE ANY LIMITATION OF ADDING in hf_register_info"?</p></div><div id="comment-62561-info" class="comment-info"><span class="comment-age">(06 Jul '17, 03:27)</span> <span class="comment-user userinfo">Abhisek</span></div></div></div><div id="comment-tools-62557" class="comment-tools"></div><div class="clear"></div><div id="comment-62557-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62569"></span>

<div id="answer-container-62569" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62569-score" class="post-score" title="current number of votes">0</div><span id="post-62569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>gtpv2.authentication_quadruplets is shown green for me when running 2.2.4. Given that it was introduced for 2.0.0, you are probably running a Wireshark version older than that (1.12.8?). Please double check the version displayed in Help -&gt; About Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '17, 05:10</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-62569" class="comments-container"><span id="62633"></span><div id="comment-62633" class="comment"><div id="post-62633-score" class="comment-score"></div><div class="comment-text"><p>No for me the same RED is shown... But after a code walk through I got one work around that the hf_register_info array is somehow not loading all registered IES in the filter box. If I copy some IEs from next half to first half then those IEs are shown GREEN in filter box. BUT THE CAUSE OF PROBLEM IS STILL UNKNOWN. P.S: I have added some new IEs as well... some of them are shown in FILTERBOX GREEN, where some are RED.</p></div><div id="comment-62633-info" class="comment-info"><span class="comment-age">(10 Jul '17, 02:01)</span> <span class="comment-user userinfo">Abhisek</span></div></div><span id="62647"></span><div id="comment-62647" class="comment"><div id="post-62647-score" class="comment-score"></div><div class="comment-text"><p>So it looks like you are modifying Wireshark source code. Does it happen with the official Wireshark 2.2.4 version without any modification? As far as I know you are the first one reporting this issue and using a freshly compiled Wireshark 2.2.4 on Fedora I cannot reproduce your issue. So it could be related to your changes.</p></div><div id="comment-62647-info" class="comment-info"><span class="comment-age">(10 Jul '17, 06:04)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-62569" class="comment-tools"></div><div class="clear"></div><div id="comment-62569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

