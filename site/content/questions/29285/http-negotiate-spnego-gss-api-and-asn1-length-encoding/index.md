+++
type = "question"
title = "HTTP Negotiate SPNEGO GSS-API and ASN.1 length encoding"
description = '''Hi, Wireshark does not seem to decode the SPNEGO GSS-API tokens correctly when they don&#x27;t contain the 0x81 or 0x82 length designator in the ASN.1 DER lengths. If the lengths don&#x27;t have the upper bit set - which means it&#x27;s just a byte of length than it isn&#x27;t decoded.'''
date = "2014-01-29T12:28:00Z"
lastmod = "2014-01-29T12:31:00Z"
weight = 29285
keywords = [ "spnego", "http", "gss-api" ]
aliases = [ "/questions/29285" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP Negotiate SPNEGO GSS-API and ASN.1 length encoding](/questions/29285/http-negotiate-spnego-gss-api-and-asn1-length-encoding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29285-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Wireshark does not seem to decode the SPNEGO GSS-API tokens correctly when they don't contain the 0x81 or 0x82 length designator in the ASN.1 DER lengths. If the lengths don't have the upper bit set - which means it's just a byte of length than it isn't decoded.</p></div><div id="question-tags" class="tags-container tags">spnego http gss-api</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '14, 12:28</strong></p><img src="https://secure.gravatar.com/avatar/0af5315eb7f584faadbb384e3f7261ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tsthrone&#39;s gravatar image" /><p>tsthrone<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tsthrone has no accepted answers">0%</span></p></div></div><div id="comments-container-29285" class="comments-container"></div><div id="comment-tools-29285" class="comment-tools"></div><div class="clear"></div><div id="comment-29285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29286"></span>

<div id="answer-container-29286" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29286-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>is this a bug report or a question?</p><ul><li>If it's a question: what is the question?<br />
</li><li>If it's a bug report, this is the wrong place for it. Please file a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '14, 12:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-29286" class="comments-container"><span id="29287"></span><div id="comment-29287" class="comment"><div id="post-29287-score" class="comment-score"></div><div class="comment-text"><p>Well it certainly looks like a bug to me. Can you confirm? I did search the bugs looking to see if it has already been reported but couldn't find anything... Should I just file a bug then?</p><p>Todd</p></div><div id="comment-29287-info" class="comment-info"><span class="comment-age">(29 Jan '14, 12:46)</span> tsthrone</div></div><span id="29289"></span><div id="comment-29289" class="comment"><div id="post-29289-score" class="comment-score"></div><div class="comment-text"><p>Please file a bug report, so others can have a look.</p></div><div id="comment-29289-info" class="comment-info"><span class="comment-age">(29 Jan '14, 13:11)</span> Kurt Knochner ♦</div></div><span id="29341"></span><div id="comment-29341" class="comment"><div id="post-29341-score" class="comment-score"></div><div class="comment-text"><p>The OP has raised bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9708">9708</a> for this.</p></div><div id="comment-29341-info" class="comment-info"><span class="comment-age">(31 Jan '14, 03:47)</span> grahamb ♦</div></div></div><div id="comment-tools-29286" class="comment-tools"></div><div class="clear"></div><div id="comment-29286-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

