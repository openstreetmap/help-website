+++
type = "question"
title = "Airpcap capture option not available"
description = '''I downloaded wireshark and the airpcap capture options are not there, how do I get these installed?'''
date = "2014-05-22T05:55:00Z"
lastmod = "2014-05-22T06:07:00Z"
weight = 32986
keywords = [ "capture", "airpcap" ]
aliases = [ "/questions/32986" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Airpcap capture option not available](/questions/32986/airpcap-capture-option-not-available)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32986-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I downloaded wireshark and the airpcap capture options are not there, how do I get these installed?</p></div><div id="question-tags" class="tags-container tags">capture airpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '14, 05:55</strong></p><img src="https://secure.gravatar.com/avatar/a30760505a1ccad6b1f939f82e9a5816?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cfd&#39;s gravatar image" /><p>cfd<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cfd has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 May '14, 06:08</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-32986" class="comments-container"></div><div id="comment-tools-32986" class="comment-tools"></div><div class="clear"></div><div id="comment-32986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32987"></span>

<div id="answer-container-32987" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32987-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Get the drivers here: <a href="https://support.riverbed.com/content/support/software/cascade/airpcap.html">https://support.riverbed.com/content/support/software/cascade/airpcap.html</a></p><p>After installation (or if you already did), remember to start Wireshark as Adminstrator. Otherwise the AirPCAP adapters are not found in the interface list.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '14, 06:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-32987" class="comments-container"><span id="32994"></span><div id="comment-32994" class="comment"><div id="post-32994-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Do I need Developers pack or windows drivers ? I have Windows 8 64 bit, the wireshark I downloaded says [wireshark 1.8.14.(v1.8.14-0-g4a6beb2 from master-1.8)].</p></div><div id="comment-32994-info" class="comment-info"><span class="comment-age">(22 May '14, 06:45)</span> cfd</div></div><span id="32997"></span><div id="comment-32997" class="comment"><div id="post-32997-score" class="comment-score"></div><div class="comment-text"><p>Drivers should be enough, unless you plan to develop software that uses AirPCAP adapters.</p></div><div id="comment-32997-info" class="comment-info"><span class="comment-age">(22 May '14, 06:59)</span> Jasper ♦♦</div></div><span id="32998"></span><div id="comment-32998" class="comment"><div id="post-32998-score" class="comment-score"></div><div class="comment-text"><p>@cfd, is there a reason for using an older version of Wireshark, the current stable version is <a href="http://www.wireshark.org/download.html">1.10.7</a>?</p></div><div id="comment-32998-info" class="comment-info"><span class="comment-age">(22 May '14, 07:04)</span> grahamb ♦</div></div><span id="32999"></span><div id="comment-32999" class="comment"><div id="post-32999-score" class="comment-score"></div><div class="comment-text"><p>This is the version I found online and I'm new at this after watching several videos I figures out I didn't have the options in the videos. I also downloaded Cain &amp; Able it missing airpcap also and CommView for wifi it cuts of my wifi when I start it, it seams Wireshark is more user friendly. I will check out version 1.10.7 where will I find it for download ?</p></div><div id="comment-32999-info" class="comment-info"><span class="comment-age">(22 May '14, 07:26)</span> cfd</div></div><span id="33000"></span><div id="comment-33000" class="comment"><div id="post-33000-score" class="comment-score"></div><div class="comment-text"><p>Supprisingly enough :-)) <a href="http://www.wireshark.org/download.html">http://www.wireshark.org/download.html</a></p><p>You're awhere that AirPcap is a HW device you need to purcase, right?</p></div><div id="comment-33000-info" class="comment-info"><span class="comment-age">(22 May '14, 07:36)</span> Anders ♦</div></div><span id="33001"></span><div id="comment-33001" class="comment not_top_scorer"><div id="post-33001-score" class="comment-score"></div><div class="comment-text"><p>I did not know that butt it figures, Thanks Jasper for all your help I may have to rattle your brain with a few more question but it won't be today I'll have to leave in a bit. cfd</p></div><div id="comment-33001-info" class="comment-info"><span class="comment-age">(22 May '14, 07:41)</span> cfd</div></div><span id="33006"></span><div id="comment-33006" class="comment not_top_scorer"><div id="post-33006-score" class="comment-score"></div><div class="comment-text"><p>sure, no problem, we're here to help. BTW if you like an answer you might want to mark it as accepted by using the checkmark button on the left next to it ;-)</p></div><div id="comment-33006-info" class="comment-info"><span class="comment-age">(22 May '14, 09:30)</span> Jasper ♦♦</div></div></div><div id="comment-tools-32987" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-32987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

