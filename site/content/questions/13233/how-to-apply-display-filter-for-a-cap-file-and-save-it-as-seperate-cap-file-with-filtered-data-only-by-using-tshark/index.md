+++
type = "question"
title = "How to apply display filter for a cap file and save it as seperate cap file with filtered data only by using Tshark..?"
description = '''Is there way to apply display filter for a cap file and save it as seperate cap file with filtered data only..? eg, 1.I have a cap file with full packets 2.Apply display filter to the first cap and save the filtered packets in to another cap file..! I need this to be done through tshark or some othe...'''
date = "2012-08-01T04:42:00Z"
lastmod = "2012-08-01T21:41:00Z"
weight = 13233
keywords = [ "save", "tshark", "display-filter" ]
aliases = [ "/questions/13233" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to apply display filter for a cap file and save it as seperate cap file with filtered data only by using Tshark..?](/questions/13233/how-to-apply-display-filter-for-a-cap-file-and-save-it-as-seperate-cap-file-with-filtered-data-only-by-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13233-score" class="post-score" title="current number of votes">0</div><span id="post-13233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there way to apply display filter for a cap file and save it as seperate cap file with filtered data only..? eg, 1.I have a cap file with full packets 2.Apply display filter to the first cap and save the filtered packets in to another cap file..!</p><p>I need this to be done through tshark or some other CLI utility...</p><p>Thanks in advance..</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-save" rel="tag" title="see questions tagged &#39;save&#39;">save</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '12, 04:42</strong></p><img src="https://secure.gravatar.com/avatar/0cc304949a3522f39e3564b6ef633717?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ArunDev&#39;s gravatar image" /><p><span>ArunDev</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ArunDev has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Aug '12, 04:45</strong> </span></p></div></div><div id="comments-container-13233" class="comments-container"></div><div id="comment-tools-13233" class="comment-tools"></div><div class="clear"></div><div id="comment-13233-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13234"></span>

<div id="answer-container-13234" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13234-score" class="post-score" title="current number of votes">2</div><span id="post-13234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can do <code>tshark -r file1.cap -R "displayfilter" -w file2.cap</code>, which reads file1, applies the filter specified after "-R" and writes it back to file2.cap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '12, 04:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13234" class="comments-container"><span id="13237"></span><div id="comment-13237" class="comment"><div id="post-13237-score" class="comment-score"></div><div class="comment-text"><p>Hi.. Thanks for your answer.... But when try to do this i am getting a message as below..!<br />
"tshark: The capture file being read can't be written as a "pcapng" file." command used: tshark -r C:\Users....\Desktop\TDP\new.cap -R "http.referer" -w C:\Users....\Desktop\file2.cap</p><p>The first cap file is captured using nmcap(NTMON) and the OS i use is windows 7</p><p>Am i doing anything wrong?</p><p>Thanks</p></div><div id="comment-13237-info" class="comment-info"><span class="comment-age">(01 Aug '12, 05:09)</span> <span class="comment-user userinfo">ArunDev</span></div></div><span id="13239"></span><div id="comment-13239" class="comment"><div id="post-13239-score" class="comment-score"></div><div class="comment-text"><p>looks like tshark has some trouble writing your nmcap format as pcap-ng. You can try and see if it works when writing to pcap format, by adding the parameter "-F libpcap" to the other parameters.</p></div><div id="comment-13239-info" class="comment-info"><span class="comment-age">(01 Aug '12, 05:52)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="13240"></span><div id="comment-13240" class="comment"><div id="post-13240-score" class="comment-score"></div><div class="comment-text"><p>I can open the netmon cap file in wirehark and save as pcap or pcapng... and found that the above command works fine.... i need everything needs to be done through cmd....is there any other way i can get the result....Thanks</p></div><div id="comment-13240-info" class="comment-info"><span class="comment-age">(01 Aug '12, 06:16)</span> <span class="comment-user userinfo">ArunDev</span></div></div><span id="13257"></span><div id="comment-13257" class="comment"><div id="post-13257-score" class="comment-score">1</div><div class="comment-text"><p>You could also use editcap to convert the files first if tshark doesn't; maybe it works with that approach. editcap also has the -F parameter which can be used to write a different file format. You could write a script that converts the file first using editcap and then filters it by using tshark.</p></div><div id="comment-13257-info" class="comment-info"><span class="comment-age">(01 Aug '12, 08:20)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="13307"></span><div id="comment-13307" class="comment"><div id="post-13307-score" class="comment-score"></div><div class="comment-text"><p>Thank you.... The Trick worked...! First i converted my nmcap to k12txt and back to pcap...Now tshark can do anything....</p></div><div id="comment-13307-info" class="comment-info"><span class="comment-age">(01 Aug '12, 21:41)</span> <span class="comment-user userinfo">ArunDev</span></div></div></div><div id="comment-tools-13234" class="comment-tools"></div><div class="clear"></div><div id="comment-13234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

