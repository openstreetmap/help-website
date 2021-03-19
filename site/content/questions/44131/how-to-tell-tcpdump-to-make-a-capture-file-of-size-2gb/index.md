+++
type = "question"
title = "how to tell tcpdump to make a capture file of size 2GB"
description = '''Hello , i need to write a command where tcp dump makes a capture of size 7GB, i tried -C 7168m but i got &quot;invalid file size&quot; error, does this command have a size limitation? and is there a way to solve this problem keeping the captures in 1 file ?'''
date = "2015-07-14T05:32:00Z"
lastmod = "2015-07-14T06:22:00Z"
weight = 44131
keywords = [ "capture-options", "tcpdump", "command", "linux" ]
aliases = [ "/questions/44131" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to tell tcpdump to make a capture file of size 2GB](/questions/44131/how-to-tell-tcpdump-to-make-a-capture-file-of-size-2gb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44131-score" class="post-score" title="current number of votes">0</div><span id="post-44131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello , i need to write a command where tcp dump makes a capture of size 7GB, i tried -C 7168m but i got "invalid file size" error, does this command have a size limitation? and is there a way to solve this problem keeping the captures in 1 file ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-options" rel="tag" title="see questions tagged &#39;capture-options&#39;">capture-options</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-command" rel="tag" title="see questions tagged &#39;command&#39;">command</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '15, 05:32</strong></p><img src="https://secure.gravatar.com/avatar/890399e77f2c0c0ff2f75ea2f43d3ff8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yas1234&#39;s gravatar image" /><p><span>yas1234</span><br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yas1234 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jul '15, 08:36</strong> </span></p></div></div><div id="comments-container-44131" class="comments-container"></div><div id="comment-tools-44131" class="comment-tools"></div><div class="clear"></div><div id="comment-44131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44133"></span>

<div id="answer-container-44133" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44133-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44133-score" class="post-score" title="current number of votes">0</div><span id="post-44133-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From the tcpdump man page:</p><p><a href="http://www.tcpdump.org/tcpdump_man.html">http://www.tcpdump.org/tcpdump_man.html</a></p><p>-C file_size = Before writing a raw packet to a savefile, check whether the file is currently larger than file_size and, if so, close the current savefile and open a new one. Savefiles after the first savefile will have the name specified with the -w flag, with a number after it, starting at 1 and continuing upward. The units of file_size are millions of bytes (1,000,000 bytes, not 1,048,576 bytes).</p><p>-W = Used in conjunction with the -C option, this will limit the number of files created to the specified number, and begin overwriting files from the beginning, thus creating a 'rotating' buffer. In addition, it will name the files with enough leading 0s to support the maximum number of files, allowing them to sort correctly. Used in conjunction with the -G option, this will limit the number of rotated dump files that get created, exiting with status 0 when reaching the limit. If used with -C as well, the behavior will result in cyclical files per timeslice.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '15, 06:17</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-44133" class="comments-container"><span id="44135"></span><div id="comment-44135" class="comment"><div id="post-44135-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "in conjunction"? Do you want to merge the separate files into one large file?</p></div><div id="comment-44135-info" class="comment-info"><span class="comment-age">(14 Jul '15, 06:22)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-44133" class="comment-tools"></div><div class="clear"></div><div id="comment-44133-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

