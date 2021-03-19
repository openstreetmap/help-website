+++
type = "question"
title = "Problem with static const value_string xxx[]"
description = '''Hi all, I have protocol where few of my header fields can have many types but my problem is: Type: Octet String (4) Values:  • (hex) 01xxxxxx : sth • (hex) 02xxxxxx : sth  where x is any hex. How should I write value_string?'''
date = "2010-09-29T07:40:00Z"
lastmod = "2010-10-01T08:33:00Z"
weight = 352
keywords = [ "value_string" ]
aliases = [ "/questions/352" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with static const value\_string xxx\[\]](/questions/352/problem-with-static-const-value_string-xxx)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-352-score" class="post-score" title="current number of votes">0</div><span id="post-352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I have protocol where few of my header fields can have many types but my problem is: Type: Octet String (4) Values: • (hex) 01xxxxxx : sth • (hex) 02xxxxxx : sth<br />
where x is any hex. How should I write value_string?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-value_string" rel="tag" title="see questions tagged &#39;value_string&#39;">value_string</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '10, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/4d850645a641fdcd2b7bb03a708f34a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wania&#39;s gravatar image" /><p><span>Wania</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wania has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-352" class="comments-container"><span id="353"></span><div id="comment-353" class="comment"><div id="post-353-score" class="comment-score"></div><div class="comment-text"><p>Sounds like a asn1 ber encoded protocol, are you using asn2wrs to create your dissector? Isn't it the case that the rest of the bits/bytes have a different meaning and you should only have a value string for part of that octet string? If not have a look at range_strings.</p></div><div id="comment-353-info" class="comment-info"><span class="comment-age">(29 Sep '10, 09:25)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="361"></span><div id="comment-361" class="comment"><div id="post-361-score" class="comment-score"></div><div class="comment-text"><p>Hi Anders,</p><p>It's not asn1, normal tcp big endian and so on. The thing is I have for example field: version with values 01xxxxxx - sth, 02xxxxxx - sth but xx08xxxx - is another version as well. It's not range_string unfortunatelly. Any ideas how i should handle this?</p><p>Wania</p></div><div id="comment-361-info" class="comment-info"><span class="comment-age">(29 Sep '10, 13:08)</span> <span class="comment-user userinfo">Wania</span></div></div><span id="400"></span><div id="comment-400" class="comment"><div id="post-400-score" class="comment-score"></div><div class="comment-text"><p>Shouldn't that be dissected like Byte 1 0000 0010 X Version 2 Byte 2 0000 1000 Y Version 8 or 0000 0010 .... .... .... .... .... .... X Version 2 .... .... 0000 1000 .... .... .... .... X Version 2 e.g as subfields of the 4 octests</p></div><div id="comment-400-info" class="comment-info"><span class="comment-age">(01 Oct '10, 08:33)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-352" class="comment-tools"></div><div class="clear"></div><div id="comment-352-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

