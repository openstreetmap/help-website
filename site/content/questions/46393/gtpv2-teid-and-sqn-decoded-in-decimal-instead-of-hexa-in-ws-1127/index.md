+++
type = "question"
title = "GTPv2 TEID and SQN decoded in Decimal instead of Hexa in WS 1.12.7"
description = '''Dear support, WS 1.12.7 is decoding GTPv2 TEID and SQN in Decimal instead of Hexa. In GTPv1 it was always in Hexa. It makes troubleshooting a bit more difficult as a conversion is necessary. Please can you let me know if there is any plans to correct this or not? Thanks a lot Br, Bulphi'''
date = "2015-10-07T07:23:00Z"
lastmod = "2015-10-07T11:21:00Z"
weight = 46393
keywords = [ "11700" ]
aliases = [ "/questions/46393" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [GTPv2 TEID and SQN decoded in Decimal instead of Hexa in WS 1.12.7](/questions/46393/gtpv2-teid-and-sqn-decoded-in-decimal-instead-of-hexa-in-ws-1127)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46393-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear support,</p><p>WS 1.12.7 is decoding GTPv2 TEID and SQN in Decimal instead of Hexa. In GTPv1 it was always in Hexa. It makes troubleshooting a bit more difficult as a conversion is necessary.</p><p>Please can you let me know if there is any plans to correct this or not?</p><p>Thanks a lot</p><p>Br, Bulphi</p></div><div id="question-tags" class="tags-container tags">11700</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '15, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/1c58e234052dcfc99b4e9deef46c7c99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="109&#39;s gravatar image" /><p>109<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="109 has no accepted answers">0%</span></p></div></div><div id="comments-container-46393" class="comments-container"></div><div id="comment-tools-46393" class="comment-tools"></div><div class="clear"></div><div id="comment-46393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46407"></span>

<div id="answer-container-46407" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46407-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In the upcoming Wireshark 2.0, TEID was changed to a 'HEX (DEC)' format display. Could you indicate what is the filter associated to this SQN parameter so as to verify?</p><p>Wireshark 1.99.9 development version (downloadable on Wireshark web site) already includes the TEID change.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '15, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-46407" class="comments-container"><span id="46413"></span><div id="comment-46413" class="comment"><div id="post-46413-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal,</p><p>Thanks a lot for your prompt answer. The filter are gtpv2.seq and gtpv2.teid where I see the values in decimal instead of Hexa.</p><p>I am currently using WS 1.12.7 which is the last official version. This is the message I get when I use the check for update version.</p><p>Br, Bulphi</p></div><div id="comment-46413-info" class="comment-info"><span class="comment-age">(07 Oct '15, 23:43)</span> 109</div></div><span id="46416"></span><div id="comment-46416" class="comment"><div id="post-46416-score" class="comment-score"></div><div class="comment-text"><p>Development versions are not proposed through the "check for update' system. You need to manually download and install it. The sequence number is still displayed as decimal. I'm gonna change it so as to display it in hexadecimal (decimal) format like the TEID.</p></div><div id="comment-46416-info" class="comment-info"><span class="comment-age">(08 Oct '15, 01:30)</span> Pascal Quantin</div></div><span id="46419"></span><div id="comment-46419" class="comment"><div id="post-46419-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal, Thanks for your reply. Please can you let me know when Ws 2.0 will be released? In case I download 1.99.9, will I still get automatic update via the "check update" function?</p><p>Br, Bulphi</p></div><div id="comment-46419-info" class="comment-info"><span class="comment-age">(08 Oct '15, 03:58)</span> 109</div></div><span id="46423"></span><div id="comment-46423" class="comment"><div id="post-46423-score" class="comment-score"></div><div class="comment-text"><p>The tentative date for Wireshark 2.0 is November the 18th. I <em>think</em> you should get an automatic update notification when coming from 1.99.9 development version, but it would be worth double checking manually.</p></div><div id="comment-46423-info" class="comment-info"><span class="comment-age">(08 Oct '15, 11:09)</span> Pascal Quantin</div></div><span id="46426"></span><div id="comment-46426" class="comment"><div id="post-46426-score" class="comment-score"></div><div class="comment-text"><p>Thank you Pascal. It is all clear now. Br, Bulphi</p></div><div id="comment-46426-info" class="comment-info"><span class="comment-age">(09 Oct '15, 00:38)</span> 109</div></div><span id="46427"></span><div id="comment-46427" class="comment not_top_scorer"><div id="post-46427-score" class="comment-score"></div><div class="comment-text"><p>If you are happy with the answer, please consider accepting it (by clicking on the check mark next to the answer) so that it can help other users when doing a search. See the faq for details.</p></div><div id="comment-46427-info" class="comment-info"><span class="comment-age">(09 Oct '15, 02:20)</span> Pascal Quantin</div></div></div><div id="comment-tools-46407" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-46407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

