+++
type = "question"
title = "Get dissector table from another plugin"
description = '''Hello, I am currently developing an dissector for an USB over network protocol. Mostly it is different from raw USB packets, but some parts are the same, so I want to dissect them with the already existing USB dissectors (e.g. &quot;usbms&quot;). I want to call them by  dissector_try_uint(...) but I cannot re...'''
date = "2014-10-14T02:09:00Z"
lastmod = "2014-10-14T13:00:00Z"
weight = 37029
keywords = [ "dissector", "dissector-table", "sub-dissector", "usb" ]
aliases = [ "/questions/37029" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Get dissector table from another plugin](/questions/37029/get-dissector-table-from-another-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37029-score" class="post-score" title="current number of votes">0</div><span id="post-37029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,<br />
I am currently developing an dissector for an USB over network protocol.<br />
Mostly it is different from raw USB packets, but some parts are the same,<br />
so I want to dissect them with the already existing USB dissectors (e.g. "usbms").<br />
I want to call them by<br />
<code>dissector_try_uint(...)</code><br />
but I cannot register the<br />
<code>register_dissector_table("usb.bulk","USB bulk endpoint", FT_UINT8, BASE_DEC)</code><br />
again because it is already done by the USB dissector itself.<br />
So do you have any solution? Is there maybe a way to get the already registered dissector table from the USB plugin?</p><p>Thanks for your help.<br />
</p><p><strong>Forgot something (maybe it is important):</strong><br />
My dissector is not named "usb", it is named "usbsrv". I just have to register "<em>usb.bulk</em>" because the needed dissectors are registered to this field.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-dissector-table" rel="tag" title="see questions tagged &#39;dissector-table&#39;">dissector-table</span> <span class="post-tag tag-link-sub-dissector" rel="tag" title="see questions tagged &#39;sub-dissector&#39;">sub-dissector</span> <span class="post-tag tag-link-usb" rel="tag" title="see questions tagged &#39;usb&#39;">usb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Oct '14, 02:09</strong></p><img src="https://secure.gravatar.com/avatar/cc56ba9bd225bd68cea09a404ecc0b6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lal12&#39;s gravatar image" /><p><span>lal12</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lal12 has 2 accepted answers">33%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Oct '14, 02:31</strong> </span></p></div></div><div id="comments-container-37029" class="comments-container"></div><div id="comment-tools-37029" class="comment-tools"></div><div class="clear"></div><div id="comment-37029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37034"></span>

<div id="answer-container-37034" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37034-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37034-score" class="post-score" title="current number of votes">2</div><span id="post-37034-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="lal12 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can retrieve the dissector table thanks to a find_dissector_table("usb.bulk") function call.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '14, 04:17</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span> </br></br></p></div></div><div id="comments-container-37034" class="comments-container"><span id="37039"></span><div id="comment-37039" class="comment"><div id="post-37039-score" class="comment-score"></div><div class="comment-text"><p>Ok now there is another Problem:<br />
While Pascal Quantins solution seems to work, the subdissector does not start no matter whether I use the <code>dissector_try_uint(...)</code> or the <code>call_dissector(...)</code> function. There is just a new "Data" item after the tree of my dissector.<br />
Maybe I missed something, is there a good example of calling a subdissector?<br />
Or could the problem be reasoned by the USBMS dissector?</p></div><div id="comment-37039-info" class="comment-info"><span class="comment-age">(14 Oct '14, 09:35)</span> <span class="comment-user userinfo">lal12</span></div></div><span id="37043"></span><div id="comment-37043" class="comment"><div id="post-37043-score" class="comment-score"></div><div class="comment-text"><p>As seen in the dissect_usb_ms_bulk() function, the dissector expects that the data parameter will contain a usb_conv_info_t structure (like what is done in epan/dissectors/packet-usb.c). If this is not the case, the packet will be rejected. You should look at what is done in packet-usb.c for creating the conversation info (get_usb_conv_info() function and its callers).</p></div><div id="comment-37043-info" class="comment-info"><span class="comment-age">(14 Oct '14, 13:00)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-37034" class="comment-tools"></div><div class="clear"></div><div id="comment-37034-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

