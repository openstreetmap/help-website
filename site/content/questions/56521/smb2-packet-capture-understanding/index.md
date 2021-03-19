+++
type = "question"
title = "SMB2 - Packet Capture - Understanding"
description = '''Just looking to improve my knowledge of SMB2 and get some answers to the protocols behaviour. I capture me opening the file t.xlsx in the _Tom Kelly folder. I capture the file being opened and the capture of that opening is clear with the create and read of the file. However at frame 114 the exact s...'''
date = "2016-10-19T20:58:00Z"
lastmod = "2016-10-25T23:32:00Z"
weight = 56521
keywords = [ "capture", "understanding", "smb2", "packet", "improve" ]
aliases = [ "/questions/56521" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SMB2 - Packet Capture - Understanding](/questions/56521/smb2-packet-capture-understanding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56521-score" class="post-score" title="current number of votes">0</div><span id="post-56521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Just looking to improve my knowledge of SMB2 and get some answers to the protocols behaviour.</p><p>I capture me opening the file t.xlsx in the _Tom Kelly folder. I capture the file being opened and the capture of that opening is clear with the create and read of the file. However at frame 114 the exact same file is opened again, even though I didn't open the file a second time. I was looking for an insight as to why this may be happening.</p><p>I see further opening and closing that SMB2 is caring out of the file and other files within the directory and understand this to be SMB2 gathering information on the file status/attributes.</p><p>I am hoping to attach the Excel spreadsheet showing the capture.</p><p>You can copy the output/images into MSPaint to get a better view of it.</p><p>Any help is greatly appreciated.</p><p>Cheers.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/SMB2Capture01_eMzKUNY.PNG" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/SMB2Capture02_bWqWFdT.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-understanding" rel="tag" title="see questions tagged &#39;understanding&#39;">understanding</span> <span class="post-tag tag-link-smb2" rel="tag" title="see questions tagged &#39;smb2&#39;">smb2</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-improve" rel="tag" title="see questions tagged &#39;improve&#39;">improve</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '16, 20:58</strong></p><img src="https://secure.gravatar.com/avatar/a64d398f30a711d53c2705c7104314b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krazynedkelly&#39;s gravatar image" /><p><span>krazynedkelly</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krazynedkelly has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Oct '16, 22:27</strong> </span></p></div></div><div id="comments-container-56521" class="comments-container"></div><div id="comment-tools-56521" class="comment-tools"></div><div class="clear"></div><div id="comment-56521-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56554"></span>

<div id="answer-container-56554" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56554-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56554-score" class="post-score" title="current number of votes">1</div><span id="post-56554-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looking at the trace file from an Excel point of view is a bit, hmm, unusual and challenging.</p><p>Sometimes individual bits in the SMB or SMB2 commands offer a bit more insight, like share options, block sizes etc.</p><p>I could imagine, that your anti-virus is scanning the file before allowing Excel to open it.</p><p>Can you confirm, if you have an anti-virus that is covering this share? You might want to exclude this folder from scans, then re-run your trace. And please, don't forget to re-enable AV.</p><p>There are other possibilities:</p><ul><li>Some mojo sotware tries to copy the file to a local drive for later offline access.</li><li>The file is being copied to the "Previous versions" graveyard.</li></ul><p>These scenarios can be investigated with local tools like the Microsoft performance monitor.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '16, 02:43</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></img></div></div><div id="comments-container-56554" class="comments-container"><span id="56668"></span><div id="comment-56668" class="comment"><div id="post-56668-score" class="comment-score"></div><div class="comment-text"><p>Cheers for the response. This is some great insight with the limited information provided. I will check to see if the anti virus software is performing the scan. Is there a way to upload the actual packet capture, I didn't see any button for such attachments. Once again thanks for the great response.</p></div><div id="comment-56668-info" class="comment-info"><span class="comment-age">(25 Oct '16, 23:07)</span> <span class="comment-user userinfo">krazynedkelly</span></div></div><span id="56672"></span><div id="comment-56672" class="comment"><div id="post-56672-score" class="comment-score"></div><div class="comment-text"><p>You can upload the either to cloudshark or some other public accessible place like Dropbox or google drive.</p></div><div id="comment-56672-info" class="comment-info"><span class="comment-age">(25 Oct '16, 23:32)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-56554" class="comment-tools"></div><div class="clear"></div><div id="comment-56554-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

