+++
type = "question"
title = "ETHERNET FRAME CHECK SEQUENCE INCORRECT"
description = '''Estimados, al realizar una captura en el puerto principal del router, se obtiene paquetes con la sgte descripcion: 464 1.410703000 10.6.20.87 10.6.13.87 TCP 64 3329→502 [SYN] Seq=0 Win=2048 Len=0 [ETHERNET FRAME CHECK SEQUENCE INCORRECT] En la ventana inferior se visualiza Frame check sequence: 0xfa...'''
date = "2014-09-30T13:35:00Z"
lastmod = "2014-09-30T14:15:00Z"
weight = 36733
keywords = [ "incorrect", "sequence" ]
aliases = [ "/questions/36733" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ETHERNET FRAME CHECK SEQUENCE INCORRECT](/questions/36733/ethernet-frame-check-sequence-incorrect)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36733-score" class="post-score" title="current number of votes">0</div><span id="post-36733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Estimados,</p><p>al realizar una captura en el puerto principal del router, se obtiene paquetes con la sgte descripcion:</p><p>464 1.410703000 10.6.20.87 10.6.13.87 TCP 64 3329→502 [SYN] Seq=0 Win=2048 Len=0 [ETHERNET FRAME CHECK SEQUENCE INCORRECT]</p><p>En la ventana inferior se visualiza</p><p>Frame check sequence: 0xfa032805 [incorrect, should be 0x041aa0e6]</p><p>FCS Bad: True Expert Info (Error/Checksum): Bad checksum Bad checksum Severity level: Error</p><p>Transmission Control Protocol, Src Port: 3329 (3329), Dst Port: 502 (502), Seq: 0, Len: 0</p><p>El analisis es a raíz de que el escaneo desde la Ip 10.6.20.87 no obtiene respuesta de la IP 10.6.13.87 y estamos tratando de determinar donde esta el problema, si es en el origen o sea en el equipo origen, en el medio de comunicación (Wan) o en el equipo destino. Gracias,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-incorrect" rel="tag" title="see questions tagged &#39;incorrect&#39;">incorrect</span> <span class="post-tag tag-link-sequence" rel="tag" title="see questions tagged &#39;sequence&#39;">sequence</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '14, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/b089c5e1a1e1fe2a76f00a5bac512189?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PETER%20F&#39;s gravatar image" /><p><span>PETER F</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PETER F has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Oct '14, 04:52</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-36733" class="comments-container"><span id="36734"></span><div id="comment-36734" class="comment"><div id="post-36734-score" class="comment-score"></div><div class="comment-text"><p>[From Google translate, with some manual editing]</p><p>Dear ,</p><p>to take a capture in the main port of the router, packets with the following description are obtained :</p><pre><code>10.6.20.87 10.6.13.87 1.410703000 464 64 3329 → 502 TCP [ SYN ] Seq = 2048 Win = 0 Len = 0 [ ETHERNET FRAME CHECK SEQUENCE INCORRECT ]</code></pre><p>In the lower window is displayed</p><pre><code>Frame check sequence : 0xfa032805 [ incorrect , Should be 0x041aa0e6 ]

FCS Bad : True Expert Info ( Error / Checksum ) : Bad Bad checksum checksum Severity level: Error

Transmission Control Protocol, Src Port : 3329 (3329) , Dst Port : 502 ( 502 ) , Seq : 0, Len : 0</code></pre><p>The following analysis is that scanning from IP 10.6.20.87 no response from the IP 10.6.13.87 and are trying to determine where the problem is , if either the source or the source computer , in the middle of communication ( Wan ) or on the target computer . Thank you ,</p></div><div id="comment-36734-info" class="comment-info"><span class="comment-age">(30 Sep '14, 14:15)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-36733" class="comment-tools"></div><div class="clear"></div><div id="comment-36733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

