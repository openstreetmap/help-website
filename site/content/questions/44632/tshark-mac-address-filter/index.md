+++
type = "question"
title = "TSHARK - mac address filter"
description = '''Troubleshooting an arp issue. Need to capture just a specific mac to see if and when it&#x27;s requesting arp. Need to see both TX/RX frames. Looking for assistance with building the tshark filter  Thanks in advance'''
date = "2015-07-30T06:23:00Z"
lastmod = "2015-08-01T01:16:00Z"
weight = 44632
keywords = [ "arp", "tshark", "mac-address" ]
aliases = [ "/questions/44632" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TSHARK - mac address filter](/questions/44632/tshark-mac-address-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44632-score" class="post-score" title="current number of votes">0</div><span id="post-44632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Troubleshooting an arp issue. Need to capture just a specific mac to see if and when it's requesting arp. Need to see both TX/RX frames.</p><p>Looking for assistance with building the tshark filter</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-mac-address" rel="tag" title="see questions tagged &#39;mac-address&#39;">mac-address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '15, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/263458deae4bb5a6773f5a7f0e1fdaa6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cfrass66&#39;s gravatar image" /><p><span>cfrass66</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cfrass66 has no accepted answers">0%</span></p></div></div><div id="comments-container-44632" class="comments-container"></div><div id="comment-tools-44632" class="comment-tools"></div><div class="clear"></div><div id="comment-44632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44633"></span>

<div id="answer-container-44633" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44633-score" class="post-score" title="current number of votes">1</div><span id="post-44633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>eth.addr == "MAC address"</p><p>example:</p><p>eth.addr == fe:ff:20:00:01:00</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '15, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-44633" class="comments-container"><span id="44635"></span><div id="comment-44635" class="comment"><div id="post-44635-score" class="comment-score"></div><div class="comment-text"><p>If the answer provided solve your problem, could you accept the solution as answered (check mark below the thumbs-up and thumbs-down). This will help others in the future.</p><p>Thank you.</p></div><div id="comment-44635-info" class="comment-info"><span class="comment-age">(30 Jul '15, 07:03)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="44653"></span><div id="comment-44653" class="comment"><div id="post-44653-score" class="comment-score"></div><div class="comment-text"><p><code>tshark -i eth4 eth.addr == fe:ff:20:00:01:00 Running as user "root" and group "root". This could be dangerous. Capturing on eth4 tshark: Invalid capture filter: "eth.addr == fe:ff:20:00:01:00"!</code></p><p>This is what i get when attempting that filter? Is there an option that needs to be set ?</p></div><div id="comment-44653-info" class="comment-info"><span class="comment-age">(30 Jul '15, 14:33)</span> <span class="comment-user userinfo">cfrass66</span></div></div><span id="44656"></span><div id="comment-44656" class="comment"><div id="post-44656-score" class="comment-score">1</div><div class="comment-text"><p><span>@cfrass66</span></p><p>tshark -i eth4 -f ether host fe:ff:20:00:01:00</p></div><div id="comment-44656-info" class="comment-info"><span class="comment-age">(30 Jul '15, 15:17)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="44659"></span><div id="comment-44659" class="comment"><div id="post-44659-score" class="comment-score"></div><div class="comment-text"><p>The reason for the error was that the original form is in <a href="https://wiki.wireshark.org/DisplayFilters">display filter</a> syntax.</p><p>The second form is in <a href="https://wiki.wireshark.org/CaptureFilters">capture filter</a> syntax, which is the default syntax if not prefixed with a flag on the tshark command line.</p></div><div id="comment-44659-info" class="comment-info"><span class="comment-age">(30 Jul '15, 15:47)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="44712"></span><div id="comment-44712" class="comment"><div id="post-44712-score" class="comment-score"></div><div class="comment-text"><p>Thank you guys!</p><h4 id="tshark--i-eth4--f-ether-host-0881f4eb814a">tshark -i eth4 -f "ether host 08:81:f4:eb:81:4a"</h4></div><div id="comment-44712-info" class="comment-info"><span class="comment-age">(31 Jul '15, 15:42)</span> <span class="comment-user userinfo">cfrass66</span></div></div><span id="44720"></span><div id="comment-44720" class="comment not_top_scorer"><div id="post-44720-score" class="comment-score"></div><div class="comment-text"><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-44720-info" class="comment-info"><span class="comment-age">(01 Aug '15, 01:16)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-44633" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-44633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

