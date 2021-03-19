+++
type = "question"
title = "IIS 8.5 Windows 2012 R2 - RST ACK problem question"
description = '''hello, we are searching for any hints or solutions. What happend ? The Webserver Application &quot;asks&quot; the server 123.123.123.123 (which is outside from our networks) and gets an response. (Authentication of an user / password) normally is see this messages: 8530 1540.845929000 10.42.1.155 123.123.123....'''
date = "2014-08-28T03:19:00Z"
lastmod = "2014-08-28T03:19:00Z"
weight = 35835
keywords = [ "rst", "8.5", "iis" ]
aliases = [ "/questions/35835" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IIS 8.5 Windows 2012 R2 - RST ACK problem question](/questions/35835/iis-85-windows-2012-r2-rst-ack-problem-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35835-score" class="post-score" title="current number of votes">0</div><span id="post-35835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello,</p><p>we are searching for any hints or solutions.</p><p>What happend ? The Webserver Application "asks" the server 123.123.123.123 (which is outside from our networks) and gets an response. (Authentication of an user / password)</p><p>normally is see this messages:</p><p>8530 1540.845929000 10.42.1.155 123.123.123.123 TLSv1 507 Application Data 8533 1540.898016000 10.42.1.155 123.123.123.123 TCP 54 52471→443 [ACK] Seq=49453 Ack=770885 Win=782080 Len=0</p><p>but very often we got these, not periodic... :</p><p>"265","146.538402000","10.42.1.155","123.123.123.123","TCP","54","52420 &gt; 443 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0" "892","223.904937000","10.42.1.155","123.123.123.123","TCP","54","52408 &gt; 443 [RST, ACK] Seq=35119 Ack=636018 Win=0 Len=0"</p><p>Transmission Control Protocol, Src Port: 52477 (52477), Dst Port: 443 (443), Seq: 751, Ack: 1088, Len: 0 .... 0000 0001 0100 = Flags: 0x014 (RST, ACK) .... .... .1.. = Reset: Set Expert Info (Warn/Sequence): Connection reset (RST)</p><p>and maybe this is related to the error messages in our application log:</p><p>ERR 530536125 26.08.2014 10:19:21 Unable to read data from the transport connection: The connection was closed. ERR 530535312 26.08.2014 10:19:21 System.IO.IOException: Unable to read data from the transport connection: The connection was <span class="__cf_email__" data-cfemail="d6b5bab9a5b3b2f896">[email protected]</span><br />
at System.Net.ConnectStream.Read(Byte[] buffer, Int32 offset, Int32 size)@ at System.IO.StreamReader.ReadBuffer()@ at System.IO.StreamReader.ReadToEnd()@ at syo2redir.ovvRedirector.ProcessRequest(String URL, HttpRequest Request)</p><p>I cant find a reason why.. Any ideas ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-8.5" rel="tag" title="see questions tagged &#39;8.5&#39;">8.5</span> <span class="post-tag tag-link-iis" rel="tag" title="see questions tagged &#39;iis&#39;">iis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '14, 03:19</strong></p><img src="https://secure.gravatar.com/avatar/684c33917df2e0bde9c62fff5e1c9def?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dormelchen&#39;s gravatar image" /><p><span>Dormelchen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dormelchen has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-35835" class="comments-container"></div><div id="comment-tools-35835" class="comment-tools"></div><div class="clear"></div><div id="comment-35835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

