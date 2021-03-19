+++
type = "question"
title = "Troubleshooting Could not create SSL/TLS secure channel"
description = '''Hi, I&#x27;m connecting using TLS 1.2 SRV 2K12 R2 but ultimately getting the message in the title. I was wondering if it&#x27;d be possible to figure out the reason via Wireshark. I&#x27;m only getting the Client&#92;Server Hello and then the Public cert exchange. The other end fully supports TLS 1.0,1.1 and 1.2 and h...'''
date = "2016-08-02T03:35:00Z"
lastmod = "2016-08-02T03:35:00Z"
weight = 54499
keywords = [ "tls", "ssl" ]
aliases = [ "/questions/54499" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Troubleshooting Could not create SSL/TLS secure channel](/questions/54499/troubleshooting-could-not-create-ssltls-secure-channel)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54499-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm connecting using TLS 1.2 SRV 2K12 R2 but ultimately getting the message in the title. I was wondering if it'd be possible to figure out the reason via Wireshark. I'm only getting the Client\Server Hello and then the Public cert exchange.</p><p>The other end fully supports TLS 1.0,1.1 and 1.2 and has A ratings on SSLLABS albeit using a SHA1 cert.</p><p>The following are wireshark output: <a href="https://www.dropbox.com/sh/yxjk3rj0lyclyn4/AADxGu6Q4tT6mzPXMJge7IGLa?dl=0">https://www.dropbox.com/sh/yxjk3rj0lyclyn4/AADxGu6Q4tT6mzPXMJge7IGLa?dl=0</a></p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">tls ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '16, 03:35</strong></p><img src="https://secure.gravatar.com/avatar/764f1cef4862ffac48685215afef4d71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xcalibur&#39;s gravatar image" /><p>xcalibur<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xcalibur has no accepted answers">0%</span></p></div></div><div id="comments-container-54499" class="comments-container"><span id="54505"></span><div id="comment-54505" class="comment"><div id="post-54505-score" class="comment-score"></div><div class="comment-text"><p>Any Alert messages after that or do you just get a TCP RST? For some reason the <code>server_name</code> field in the Server Hello is empty, that could be a misconfiguration on the server part that rejects your hostname. I would look into that</p></div><div id="comment-54505-info" class="comment-info"><span class="comment-age">(02 Aug '16, 05:29)</span> Lekensteyn</div></div><span id="54507"></span><div id="comment-54507" class="comment"><div id="post-54507-score" class="comment-score"></div><div class="comment-text"><p>I actually dont see anything after or before it (using "ssl" as the filter query). But I will surely check with the other side to make sure they dont use some sort of a whitelist.</p></div><div id="comment-54507-info" class="comment-info"><span class="comment-age">(02 Aug '16, 06:09)</span> xcalibur</div></div><span id="54508"></span><div id="comment-54508" class="comment"><div id="post-54508-score" class="comment-score"></div><div class="comment-text"><p>Then again had it been whitelisting then I wouldnt be able to get neither HELLOs.</p></div><div id="comment-54508-info" class="comment-info"><span class="comment-age">(02 Aug '16, 06:16)</span> xcalibur</div></div><span id="54533"></span><div id="comment-54533" class="comment"><div id="post-54533-score" class="comment-score"></div><div class="comment-text"><p>I uploaded the full PCAP if it's any good...</p></div><div id="comment-54533-info" class="comment-info"><span class="comment-age">(03 Aug '16, 00:48)</span> xcalibur</div></div><span id="54545"></span><div id="comment-54545" class="comment"><div id="post-54545-score" class="comment-score"></div><div class="comment-text"><p>The pcap is more helpful, although it just shows the client closing the connection with a RST just after the server sent the "Server Hello Done".</p><p>You might also note that there is also a lot of other traffic in the capture, Windows SMB and SQL Server stuff that you might not want to have shown to the world.</p></div><div id="comment-54545-info" class="comment-info"><span class="comment-age">(03 Aug '16, 02:17)</span> grahamb ♦</div></div><span id="54549"></span><div id="comment-54549" class="comment not_top_scorer"><div id="post-54549-score" class="comment-score"></div><div class="comment-text"><p>Thanks for letting me know. I thought it saved just the selected packaets. Fixed now.</p></div><div id="comment-54549-info" class="comment-info"><span class="comment-age">(03 Aug '16, 03:01)</span> xcalibur</div></div></div><div id="comment-tools-54499" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-54499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

