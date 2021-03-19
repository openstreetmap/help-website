+++
type = "question"
title = "Why are tmp files generated when using tshark&#x27;s -w option?"
description = '''I have a tshark process using the -b duration:[seconds], -b files:[numberoffiles], and -w [outputfile] options.  The process writes to the output files as expected  Unexpectedly, however, it continues to generate /tmp/ files.  I had thought that because the process is writing to an output file that ...'''
date = "2017-02-09T07:07:00Z"
lastmod = "2017-02-09T08:39:00Z"
weight = 59286
keywords = [ "tmp", "tmpfile", "tshark" ]
aliases = [ "/questions/59286" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why are tmp files generated when using tshark's -w option?](/questions/59286/why-are-tmp-files-generated-when-using-tsharks-w-option)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59286-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59286-score" class="post-score" title="current number of votes">0</div><span id="post-59286-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a tshark process using the <strong>-b duration:[seconds]</strong>, <strong>-b files:[numberoffiles]</strong>, and <strong>-w [outputfile]</strong> options.</p><p>The process writes to the output files as expected</p><p>Unexpectedly, however, it continues to generate /tmp/ files.</p><p>I had thought that because the process is writing to an output file that the tmp file was not necessary.</p><p>Is tshark working as designed? Do I just need to create a local cron job to cleanup the /tmp/ directory?</p><p>For clarification, the version I'm running is part of wireshark-1.8.10-17.el6.x86_64 package.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tmp" rel="tag" title="see questions tagged &#39;tmp&#39;">tmp</span> <span class="post-tag tag-link-tmpfile" rel="tag" title="see questions tagged &#39;tmpfile&#39;">tmpfile</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '17, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/8254293c50f4995b29b0ff8746f465db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="deldalton&#39;s gravatar image" /><p><span>deldalton</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="deldalton has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Feb '17, 08:40</strong> </span></p></div></div><div id="comments-container-59286" class="comments-container"><span id="59294"></span><div id="comment-59294" class="comment"><div id="post-59294-score" class="comment-score"></div><div class="comment-text"><p>Version of tshark?</p></div><div id="comment-59294-info" class="comment-info"><span class="comment-age">(09 Feb '17, 08:07)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="59296"></span><div id="comment-59296" class="comment"><div id="post-59296-score" class="comment-score"></div><div class="comment-text"><p>Version is wireshark-1.8.10-17.el6.x86_64.</p></div><div id="comment-59296-info" class="comment-info"><span class="comment-age">(09 Feb '17, 08:39)</span> <span class="comment-user userinfo">deldalton</span></div></div></div><div id="comment-tools-59286" class="comment-tools"></div><div class="clear"></div><div id="comment-59286-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

