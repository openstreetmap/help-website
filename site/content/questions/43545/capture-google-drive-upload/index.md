+++
type = "question"
title = "Capture Google Drive Upload?"
description = '''As I know this far, I need to know which is the IP address of the google drive upload. But I can&#x27;t find one. Is this correct way? Thank you.'''
date = "2015-06-25T07:31:00Z"
lastmod = "2015-06-25T08:21:00Z"
weight = 43545
keywords = [ "capture", "upload" ]
aliases = [ "/questions/43545" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture Google Drive Upload?](/questions/43545/capture-google-drive-upload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43545-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As I know this far, I need to know which is the IP address of the google drive upload. But I can't find one. Is this correct way? Thank you.</p></div><div id="question-tags" class="tags-container tags">capture upload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '15, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/7c4136ecf97e9e0f38e26d2e5cebcafe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rommy&#39;s gravatar image" /><p>Rommy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rommy has no accepted answers">0%</span></p></div></div><div id="comments-container-43545" class="comments-container"></div><div id="comment-tools-43545" class="comment-tools"></div><div class="clear"></div><div id="comment-43545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="43548"></span>

<div id="answer-container-43548" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43548-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Determine the IP address of your machine</li><li>In Wireshark, select Capture / options</li><li>Select the interface that connect to the LAN</li><li>Enter the following capture filter: host &lt;your-ip-address&gt;</li><li>Start capturing</li><li>Go to Google drive and upload a file</li></ol><p>You should only see traffic to/from your computer. Now find the TCP traffic to/from Internet. You can confirm by right-clicking on one of the packets and select "Follow TCP Stream" In the analysis screen, you should see "upload.docs.google.com"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '15, 08:18</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-43548" class="comments-container"></div><div id="comment-tools-43548" class="comment-tools"></div><div class="clear"></div><div id="comment-43548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43549"></span>

<div id="answer-container-43549" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43549-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Google drive is hosted in the Google CDN (1e100.net) and you will get different IPs for drive.google.com depending on the geographical region you are in. You can obviously resolve drive.google.com to get the IP address for your region and then capture traffic to that IP address. <strong>However</strong> the whole traffic to the google servers is encrypted (https). You will be able to see that something is being transmitted to the google servers, but you won't see <strong>what</strong> is being uploaded. If you need that, please take a look at <a href="http://www.telerik.com/fiddler">Fiddler</a> (or similar tools).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '15, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jun '15, 08:25</p></div></div><div id="comments-container-43549" class="comments-container"><span id="43589"></span><div id="comment-43589" class="comment"><div id="post-43589-score" class="comment-score"></div><div class="comment-text"><p>I don't know what to say. Thank you very much :)</p></div><div id="comment-43589-info" class="comment-info"><span class="comment-age">(26 Jun '15, 05:17)</span> Rommy</div></div><span id="43600"></span><div id="comment-43600" class="comment"><div id="post-43600-score" class="comment-score"></div><div class="comment-text"><p>@ Rommy</p><p>I don't know which answer your comment, which I converted from an "answer" belongs to.</p><p>Can you please accept the answer that helped you most by clicking the checkmark icon by that answer. This also helps others with the same question later.</p></div><div id="comment-43600-info" class="comment-info"><span class="comment-age">(27 Jun '15, 07:42)</span> grahamb ♦</div></div></div><div id="comment-tools-43549" class="comment-tools"></div><div class="clear"></div><div id="comment-43549-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

