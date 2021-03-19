+++
type = "question"
title = "Total Fields can be exported to CSV file"
description = '''Hi All, I am working on tshark -T option to export fields to .csv file. I successfully performed the conversion using tshark -r input.pcap -T fields -e field_name -E separator=,  I have tried field name ip.src , ip.dst and frame.number. I would like to know the all field names which I can use in exp...'''
date = "2014-02-16T21:52:00Z"
lastmod = "2014-02-20T05:44:00Z"
weight = 29921
keywords = [ "field", "csv", "tshark" ]
aliases = [ "/questions/29921" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Total Fields can be exported to CSV file](/questions/29921/total-fields-can-be-exported-to-csv-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29921-score" class="post-score" title="current number of votes">0</div><span id="post-29921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All, I am working on tshark -T option to export fields to .csv file. I successfully performed the conversion using tshark -r input.pcap -T fields -e field_name -E separator=,</p><p>I have tried field name ip.src , ip.dst and frame.number. I would like to know the all field names which I can use in exporting .csv file.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-field" rel="tag" title="see questions tagged &#39;field&#39;">field</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '14, 21:52</strong></p><img src="https://secure.gravatar.com/avatar/904e19785874be39705426e578c4c029?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aditi&#39;s gravatar image" /><p><span>Aditi</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aditi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Feb '14, 02:04</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-29921" class="comments-container"></div><div id="comment-tools-29921" class="comment-tools"></div><div class="clear"></div><div id="comment-29921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29926"></span>

<div id="answer-container-29926" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29926-score" class="post-score" title="current number of votes">1</div><span id="post-29926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Aditi has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are lots of fields, use <code>tshark -G fields</code> to list them all</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '14, 02:09</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-29926" class="comments-container"><span id="29927"></span><div id="comment-29927" class="comment"><div id="post-29927-score" class="comment-score"></div><div class="comment-text"><p>or check the online docs</p><blockquote><p><a href="http://www.wireshark.org/docs/dfref">http://www.wireshark.org/docs/dfref</a></p></blockquote></div><div id="comment-29927-info" class="comment-info"><span class="comment-age">(17 Feb '14, 02:17)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="30038"></span><div id="comment-30038" class="comment"><div id="post-30038-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt,</p><p>As you suggested I got all the field list, upon checking them, I find lot other fields in all protocols, say IP protocol, I found ip.geoip.city and ip.src_rt. As per my knowledge, there is no filed for geoip.city or src_rt in IP protocol header. I could not understand that from where wireshark/ tshark will capture all this details if it is not at all available in packet itself....</p></div><div id="comment-30038-info" class="comment-info"><span class="comment-age">(19 Feb '14, 22:37)</span> <span class="comment-user userinfo">Aditi</span></div></div><span id="30042"></span><div id="comment-30042" class="comment"><div id="post-30042-score" class="comment-score"></div><div class="comment-text"><p>Some fields are synthesized by Wireshark from the information in the capture and sometimes using external sources.</p><p>In the case of the two fields mentioned, <code>ip.geoip.city</code> is set via <a href="http://wiki.wireshark.org/HowToUseGeoIP">ip to geographic location lookup</a> and the second field <code>ip.src_rt</code> is set if the packet contains IP source routing options, either LSSR or SSRR, see <a href="http://tools.ietf.org/html/rfc791#page-11">RFC 791</a></p></div><div id="comment-30042-info" class="comment-info"><span class="comment-age">(20 Feb '14, 05:44)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-29926" class="comment-tools"></div><div class="clear"></div><div id="comment-29926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

