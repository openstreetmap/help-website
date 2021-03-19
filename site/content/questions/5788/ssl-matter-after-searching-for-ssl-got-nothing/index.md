+++
type = "question"
title = "SSL matter - after searching for &#x27;ssl&#x27; got nothing"
description = '''SSL matter - after searching for &#x27;ssl&#x27; got nothing - used wireless laptop After Login (recorded always by WireShark) to Paypal and GoDaddy.com, I get some data in wireshark trace, but after searching for &#x27;ssl&#x27; I get nothing, well where is the problem? WireShark sniffs all packets independently of wh...'''
date = "2011-08-21T12:02:00Z"
lastmod = "2011-08-23T21:39:00Z"
weight = 5788
keywords = [ "ssl" ]
aliases = [ "/questions/5788" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL matter - after searching for 'ssl' got nothing](/questions/5788/ssl-matter-after-searching-for-ssl-got-nothing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5788-score" class="post-score" title="current number of votes">0</div><span id="post-5788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>SSL matter - after searching for 'ssl' got nothing - used wireless laptop After Login (recorded always by WireShark) to Paypal and GoDaddy.com, I get some data in wireshark trace, but after searching for 'ssl' I get nothing, well where is the problem?</p><p>WireShark sniffs all packets independently of where belog in Layer Stack?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '11, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/83f6c157853b4626dfd333b3a7f6fd9c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lse123ws&#39;s gravatar image" /><p><span>lse123ws</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lse123ws has no accepted answers">0%</span></p></div></div><div id="comments-container-5788" class="comments-container"><span id="5799"></span><div id="comment-5799" class="comment"><div id="post-5799-score" class="comment-score"></div><div class="comment-text"><p>WireShark sniffs all packets independently of where belong in Layer Stack? all packets go the screen of wireshark without choose what's layer's packers to appear? later can apply filter? these are true?</p></div><div id="comment-5799-info" class="comment-info"><span class="comment-age">(22 Aug '11, 02:25)</span> <span class="comment-user userinfo">lse123ws</span></div></div><span id="5834"></span><div id="comment-5834" class="comment"><div id="post-5834-score" class="comment-score"></div><div class="comment-text"><p>Wireshark captures link-layer packets; if you haven't specified a capture filter, it captures all packets, regardless of what protocols are in the packets above the link layer. You can then apply a display filter to select packets that contain a particular protocol.</p><p>If there are packets in the capture that Wireshark recognizes as SSL, a display filter of "ssl" will show them. By default, Wireshark will recognize HTTP packets to or from port 443 as HTTP-over-SSL packets; is your "Login" to those services over HTTP or some other protocol?</p></div><div id="comment-5834-info" class="comment-info"><span class="comment-age">(23 Aug '11, 21:39)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-5788" class="comment-tools"></div><div class="clear"></div><div id="comment-5788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

