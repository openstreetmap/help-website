+++
type = "question"
title = "get_field_data: code should not be reached (PDML File)"
description = '''Hello all--  I am trying to export pdml using wireshark for a trace containing h245 traffic. The export from GUI crashes while trying to export.  I then tried tshark -r tandberg.pcap -T pdml; It gave me error  ERROR:print.c:715:get_field_data: code should not be reached I have tried to search the er...'''
date = "2011-04-11T13:30:00Z"
lastmod = "2011-04-13T08:24:00Z"
weight = 3453
keywords = [ "xml", "get_field_data", "pdml" ]
aliases = [ "/questions/3453" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [get\_field\_data: code should not be reached (PDML File)](/questions/3453/get_field_data-code-should-not-be-reached-pdml-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3453-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3453-score" class="post-score" title="current number of votes">0</div><span id="post-3453-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all--</p><p>I am trying to export pdml using wireshark for a trace containing h245 traffic. The export from GUI crashes while trying to export.</p><p>I then tried tshark -r tandberg.pcap -T pdml; It gave me error</p><p>ERROR:print.c:715:get_field_data: code should not be reached</p><p>I have tried to search the error and a bug report was filed</p><p>http://www.mail-archive.com/<span class="__cf_email__" data-cfemail="4e39273c2b3d262f3c25632c3b293d0e39273c2b3d262f3c2560213c29">[email protected]</span>/msg22849.html</p><p>It does say that -V should be able to handle it, however, the output generated with -V option does not contain XML file.</p><p>I will be grateful for any help by community.</p><p>Thanking you in advance</p><p>Regards Lonex</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-get_field_data" rel="tag" title="see questions tagged &#39;get_field_data&#39;">get_field_data</span> <span class="post-tag tag-link-pdml" rel="tag" title="see questions tagged &#39;pdml&#39;">pdml</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '11, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/58323607e4a041f766b20930c7e50d5c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonex&#39;s gravatar image" /><p><span>lonex</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonex has no accepted answers">0%</span></p></div></div><div id="comments-container-3453" class="comments-container"><span id="3458"></span><div id="comment-3458" class="comment"><div id="post-3458-score" class="comment-score"></div><div class="comment-text"><p>I was able to fix it, by downloading the code and commenting the portion where the error was occurring.</p></div><div id="comment-3458-info" class="comment-info"><span class="comment-age">(11 Apr '11, 17:44)</span> <span class="comment-user userinfo">lonex</span></div></div><span id="3474"></span><div id="comment-3474" class="comment"><div id="post-3474-score" class="comment-score"></div><div class="comment-text"><p>You'd better issue a bug report at https://bugs.wireshark.org/bugzilla/ in order to get the code fixed.</p></div><div id="comment-3474-info" class="comment-info"><span class="comment-age">(12 Apr '11, 22:59)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="3483"></span><div id="comment-3483" class="comment"><div id="post-3483-score" class="comment-score"></div><div class="comment-text"><p>It's bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3821">3821</a>.</p></div><div id="comment-3483-info" class="comment-info"><span class="comment-age">(13 Apr '11, 08:24)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-3453" class="comment-tools"></div><div class="clear"></div><div id="comment-3453-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

