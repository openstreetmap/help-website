+++
type = "question"
title = "How to dissect wlan challenge info packets?"
description = '''I want to dissect challenge and auth process as below. After analyzing, I find packets 16806~16814 in the file, but how to dissect them with tshark/wireshark? Are they sccp packages? The processes 8~13 are what I concerned.  The file: http://www.cloudshark.org/captures/689877c7f961?filter=ip.addr%20...'''
date = "2013-12-03T17:43:00Z"
lastmod = "2013-12-11T18:40:00Z"
weight = 27737
keywords = [ "challenge", "wlan" ]
aliases = [ "/questions/27737" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to dissect wlan challenge info packets?](/questions/27737/how-to-dissect-wlan-challenge-info-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27737-score" class="post-score" title="current number of votes">0</div><span id="post-27737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to dissect challenge and auth process as below. After analyzing, I find packets 16806~16814 in the file, but how to dissect them with tshark/wireshark? Are they sccp packages?</p><p>The processes 8~13 are what I concerned. <img src="https://osqa-ask.wireshark.org/upfiles/proc.jpg" alt="alt text" /> The file: <a href="http://www.cloudshark.org/captures/689877c7f961?filter=ip.addr%20eq%20192.168.1.21">http://www.cloudshark.org/captures/689877c7f961?filter=ip.addr%20eq%20192.168.1.21</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-challenge" rel="tag" title="see questions tagged &#39;challenge&#39;">challenge</span> <span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '13, 17:43</strong></p><img src="https://secure.gravatar.com/avatar/13679628c84abac93be65773340d2589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="metamatrix&#39;s gravatar image" /><p><span>metamatrix</span><br />
<span class="score" title="56 reputation points">56</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="metamatrix has one accepted answer">100%</span></p></img></div></div><div id="comments-container-27737" class="comments-container"><span id="27966"></span><div id="comment-27966" class="comment"><div id="post-27966-score" class="comment-score"></div><div class="comment-text"><p>Any one have ideas?</p></div><div id="comment-27966-info" class="comment-info"><span class="comment-age">(09 Dec '13, 21:53)</span> <span class="comment-user userinfo">metamatrix</span></div></div></div><div id="comment-tools-27737" class="comment-tools"></div><div class="clear"></div><div id="comment-27737-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27970"></span>

<div id="answer-container-27970" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27970-score" class="post-score" title="current number of votes">1</div><span id="post-27970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="metamatrix has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From the capture file I conclude</p><ul><li>192.168.1.89 is your <a href="http://www.h3c.com/portal/Products___Solutions/Products/WLAN/H3C_WX5000_Series_Access_Controllers/">H3C wireless access controller</a></li><li>192.168.1.21 is your Radius server, running in a virtual machine (maybe on some windows system)</li></ul><p>Now, there are those packets you mentioned: #16806 - #16814</p><p>You see communication between those two systems.</p><ul><li>Radius: 192.168.1.89 -&gt; 192.168.1.21</li><li>Unknown Protocol: 192.168.1.89:2000 (sccp) &lt;--&gt; 192.168.1.21:50100</li></ul><p>So, it <strong>looks like</strong> there is sccp (Cisco Skinny) involved, due to port 2000. However, I believe the communication is from 192.168.1.89:2000 (sccp) --&gt; 192.168.1.21:50100. So, port 2000 is just a random <strong>source port</strong> and thus <strong>not related to Skinny</strong>. The data in the frames do not fit the Skinny protocol, as the first 4 bytes should be the length of the Skinny payload and if you look at the frames, that's not gonna work (length is way too large).</p><p>So, I guess this is a custom protocol used by your H3C wireless controller that is unknown to Wireshark.</p><p>You should be able to figure out which service accepts data on port 50100 on the Radius server (192.168.1.21) by running these commands</p><p><strong>Windows</strong> (as Administartor from an elevated DOS box)</p><blockquote><p>netstat -nab | more</p></blockquote><p>Then look for the string ":50100" and post those lines +/-2 here.</p><p>It will look similar to this</p><pre><code>  UDP    192.168.1.21:50100    *:*                                    1
  [xxxxx.exe]</code></pre><p><strong>Linux</strong> (as root)</p><blockquote><p>sudo netstat -nap | grep ":50100"</p></blockquote><p>That will help to understand which component is using the (yet unknown) protocol. With that information you can search the documentation of the H3C wireless controller (search for port 50100) or ask in their support forum.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '13, 04:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Dec '13, 06:58</strong> </span></p></div></div><div id="comments-container-27970" class="comments-container"><span id="27987"></span><div id="comment-27987" class="comment"><div id="post-27987-score" class="comment-score"></div><div class="comment-text"><p>Thank you, Kurt. I think the unkown protocol using port 2000 is not a coincidence. Since I found a document that mentions challenge info also using port 2000. (<a href="http://wenku.baidu.com/view/e0beea2f647d27284b73513f.html?qq-pf-to=pcqq.c2c">http://wenku.baidu.com/view/e0beea2f647d27284b73513f.html?qq-pf-to=pcqq.c2c</a> page 10).And I also found first 2 bytes of the data possibly mean some type. So I think I can use the port 2000 and first 2 bytes of data to distinguish the step of wlan user logon process, can I?</p></div><div id="comment-27987-info" class="comment-info"><span class="comment-age">(10 Dec '13, 21:34)</span> <span class="comment-user userinfo">metamatrix</span></div></div><span id="27988"></span><div id="comment-27988" class="comment"><div id="post-27988-score" class="comment-score"></div><div class="comment-text"><p>Thank you, Kurt. I've found the H3C portal protocol specification :) (<a href="http://wenku.baidu.com/view/8a698abec77da26925c5b0b5.html).">http://wenku.baidu.com/view/8a698abec77da26925c5b0b5.html).</a></p></div><div id="comment-27988-info" class="comment-info"><span class="comment-age">(10 Dec '13, 21:57)</span> <span class="comment-user userinfo">metamatrix</span></div></div><span id="28005"></span><div id="comment-28005" class="comment"><div id="post-28005-score" class="comment-score"></div><div class="comment-text"><p>Is there also an english version of the document?</p></div><div id="comment-28005-info" class="comment-info"><span class="comment-age">(11 Dec '13, 07:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="28030"></span><div id="comment-28030" class="comment"><div id="post-28030-score" class="comment-score"></div><div class="comment-text"><p>I'm afraid there is no English version of the document that can be found. Chinese version is shared by somebody on internet, and in baidu doc most of documents are in Chinese.</p></div><div id="comment-28030-info" class="comment-info"><span class="comment-age">(11 Dec '13, 18:40)</span> <span class="comment-user userinfo">metamatrix</span></div></div></div><div id="comment-tools-27970" class="comment-tools"></div><div class="clear"></div><div id="comment-27970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

