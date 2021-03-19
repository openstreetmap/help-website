+++
type = "question"
title = "TCP Checksum Validation Disabled"
description = '''Is there any reason why the TCP checksum validation would be disabled. I believe I spotted a host communicating to a CnC server then being redirected to another potential drive by download site.  The TCP validation disabled checksum is for incoming traffic from the potential CnC server. Thanks'''
date = "2011-02-09T02:26:00Z"
lastmod = "2011-02-10T02:45:00Z"
weight = 2253
keywords = [ "checksum", "tcp" ]
aliases = [ "/questions/2253" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Checksum Validation Disabled](/questions/2253/tcp-checksum-validation-disabled)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2253-score" class="post-score" title="current number of votes">0</div><span id="post-2253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any reason why the TCP checksum validation would be disabled. I believe I spotted a host communicating to a CnC server then being redirected to another potential drive by download site.</p><p>The TCP validation disabled checksum is for incoming traffic from the potential CnC server.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-checksum" rel="tag" title="see questions tagged &#39;checksum&#39;">checksum</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '11, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/66777941e85ed6b3f729d2ba44d720da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eygobigmoney&#39;s gravatar image" /><p><span>eygobigmoney</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eygobigmoney has no accepted answers">0%</span></p></div></div><div id="comments-container-2253" class="comments-container"></div><div id="comment-tools-2253" class="comment-tools"></div><div class="clear"></div><div id="comment-2253-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2254"></span>

<div id="answer-container-2254" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2254-score" class="post-score" title="current number of votes">2</div><span id="post-2254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes. The reason is that Wireshark is very often used to capture the network frames of the same PC that is running Wireshark. This usually results in the checksums of outgoing frames being incorrect since they are only calculated for transmission by the network card after they were already recorded by Wireshark. To avoid constant "checksum error" messages it was decided to have the checksum validation disabled by default.</p><p>It may sound stupid to disabled checkum validation since we want to find damaged packets with Wireshark when tracking down errors. But the fact is that frames with damaged checksums won't survive much long anyway since every switch or router will probably drop them for being defective - and still, if the frame makes it to your network card it will still drop it before Wireshark even sees it. This is the reason why some commercial sniffers have specialized NIC drivers for certain cards that will allow capturing damaged frames with them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '11, 03:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2254" class="comments-container"></div><div id="comment-tools-2254" class="comment-tools"></div><div class="clear"></div><div id="comment-2254-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2260"></span>

<div id="answer-container-2260" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2260-score" class="post-score" title="current number of votes">0</div><span id="post-2260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Although Jasper answered "Why are TCP checksums disabled by default" perfectly, I believe your question might not have been answered. Or maybe I just got confused.</p><p>I believe your question is how to detect if someone spoofed another host and hijacked your session? Well, this is not the purpose of TCP checksums. It is also not so easy to detect, as it can be done at several levels.</p><p>I'm curious though, were you able to spot this by enabling TCP checksum checking? And how?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '11, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2260" class="comments-container"><span id="2268"></span><div id="comment-2268" class="comment"><div id="post-2268-score" class="comment-score"></div><div class="comment-text"><p>I think when he's talking about CnC servers he means that he suspects a local PC being infected by a botnet agent trying to contact its Command and Control server. To verify that you'd need computer/network forensics. I don't think that it has anything to do with spoofed sessions - but you're right, I only answered in regard to the CRC topic :-)</p></div><div id="comment-2268-info" class="comment-info"><span class="comment-age">(10 Feb '11, 02:45)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-2260" class="comment-tools"></div><div class="clear"></div><div id="comment-2260-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

