+++
type = "question"
title = "Can we Invoke wireshark through API"
description = '''Hi I have client-server application. In server, the pcap, files will be available and in client I will list all the pcap files. User can select a pcap file and open it in wireshark. Now the problem is I can send whole wireshark application to client to view the pcap.I would like to know : 1. Can wir...'''
date = "2011-06-24T02:58:00Z"
lastmod = "2011-06-24T11:24:00Z"
weight = 4719
keywords = [ "wiresharkapi" ]
aliases = [ "/questions/4719" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can we Invoke wireshark through API](/questions/4719/can-we-invoke-wireshark-through-api)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4719-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4719-score" class="post-score" title="current number of votes">0</div><span id="post-4719-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have client-server application. In server, the pcap, files will be available and in client I will list all the pcap files. User can select a pcap file and open it in wireshark. Now the problem is I can send whole wireshark application to client to view the pcap.I would like to know : 1. Can wireshark be invoked on IE or Mozzila. 2. Is there any API, so that I can call it from server.</p><p>Please help.</p><p>Thanks, Kumar</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wiresharkapi" rel="tag" title="see questions tagged &#39;wiresharkapi&#39;">wiresharkapi</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '11, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/379fd77e13559e76c5c88b3fb0ff897a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KumarABCD&#39;s gravatar image" /><p><span>KumarABCD</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KumarABCD has no accepted answers">0%</span></p></div></div><div id="comments-container-4719" class="comments-container"></div><div id="comment-tools-4719" class="comment-tools"></div><div class="clear"></div><div id="comment-4719-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4720"></span>

<div id="answer-container-4720" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4720-score" class="post-score" title="current number of votes">0</div><span id="post-4720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could prepare a Wireshark portable version your users can call from any shared directory if you want your users to use the GUI client without having to install it everywhere.</p><p>Otherwise you might want to take a look at cloudshark at <a href="http://www.cloudshark.org/">http://www.cloudshark.org/</a>, maybe their appliance is something that works for you. It is designed to allow concurrent access to centrally stored pcap files by web browser.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '11, 03:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jun '11, 03:03</strong> </span></p></div></div><div id="comments-container-4720" class="comments-container"><span id="4721"></span><div id="comment-4721" class="comment"><div id="post-4721-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper. Where I can get more information for Option 1.</p></div><div id="comment-4721-info" class="comment-info"><span class="comment-age">(24 Jun '11, 03:09)</span> <span class="comment-user userinfo">KumarABCD</span></div></div><span id="4722"></span><div id="comment-4722" class="comment"><div id="post-4722-score" class="comment-score"></div><div class="comment-text"><p>Download the portable version at http://www.wireshark.org/download.html, download the "Portable App" version and install it into any shared directory your users can access. After installation it can be called from any workstation that has access to the directory.</p></div><div id="comment-4722-info" class="comment-info"><span class="comment-age">(24 Jun '11, 03:12)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="4730"></span><div id="comment-4730" class="comment"><div id="post-4730-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper. Will this portable version can be invoked from a solaris workstation. or is there any seperate solaris portable version that can be accessed by Windows client/workstation. My Client may be a windows/unix workstation. So will be OS compatible?</p></div><div id="comment-4730-info" class="comment-info"><span class="comment-age">(24 Jun '11, 07:36)</span> <span class="comment-user userinfo">KumarABCD</span></div></div><span id="4736"></span><div id="comment-4736" class="comment"><div id="post-4736-score" class="comment-score"></div><div class="comment-text"><p>The "Portable App" stuff is Windows-only.</p></div><div id="comment-4736-info" class="comment-info"><span class="comment-age">(24 Jun '11, 11:24)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-4720" class="comment-tools"></div><div class="clear"></div><div id="comment-4720-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4727"></span>

<div id="answer-container-4727" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4727-score" class="post-score" title="current number of votes">0</div><span id="post-4727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe this can be of help: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5785">Enhancement bug 5785</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '11, 06:52</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4727" class="comments-container"></div><div id="comment-tools-4727" class="comment-tools"></div><div class="clear"></div><div id="comment-4727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

