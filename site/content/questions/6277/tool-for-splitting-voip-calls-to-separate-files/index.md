+++
type = "question"
title = "Tool for splitting voip calls to separate files"
description = '''Hi, I have to deal with very large pcap files which include many voip (h323, sip, isup) calls. Of course it takes a lot time to open these large files and find the correct call on a desktop computer. Is there a tool to create individual pcap files for each voip call from a large file ? Thanks.'''
date = "2011-09-12T03:59:00Z"
lastmod = "2011-09-14T22:42:00Z"
weight = 6277
keywords = [ "pcap", "split", "voip" ]
aliases = [ "/questions/6277" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tool for splitting voip calls to separate files](/questions/6277/tool-for-splitting-voip-calls-to-separate-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6277-score" class="post-score" title="current number of votes">1</div><span id="post-6277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have to deal with very large pcap files which include many voip (h323, sip, isup) calls. Of course it takes a lot time to open these large files and find the correct call on a desktop computer. Is there a tool to create individual pcap files for each voip call from a large file ?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '11, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/678e3cab9622b907d1484c4ecf37094d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrmrmrmr&#39;s gravatar image" /><p><span>mrmrmrmr</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrmrmrmr has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Sep '11, 08:06</strong> </span></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-6277" class="comments-container"></div><div id="comment-tools-6277" class="comment-tools"></div><div class="clear"></div><div id="comment-6277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6280"></span>

<div id="answer-container-6280" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6280-score" class="post-score" title="current number of votes">1</div><span id="post-6280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use Wireshark Lua to do this. Try this <a href="http://wiki.wireshark.org/Lua/Examples#Dump_VoIP_calls_into_separate_files">Lua script</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '11, 05:50</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p><span>bstn</span><br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div></div><div id="comments-container-6280" class="comments-container"><span id="6288"></span><div id="comment-6288" class="comment"><div id="post-6288-score" class="comment-score"></div><div class="comment-text"><p>Thanks. It seems that this example only covers SIP calls. Where can I find more examples ? maybe an H225 , Q931 , ISUP equivalent ?</p><p>Lua is something I didn't know. It seems we can make use of it, but I need to learn a lot.</p></div><div id="comment-6288-info" class="comment-info"><span class="comment-age">(12 Sep '11, 08:09)</span> <span class="comment-user userinfo">mrmrmrmr</span></div></div><span id="6381"></span><div id="comment-6381" class="comment"><div id="post-6381-score" class="comment-score"></div><div class="comment-text"><p>any other suggestions ?</p></div><div id="comment-6381-info" class="comment-info"><span class="comment-age">(14 Sep '11, 22:42)</span> <span class="comment-user userinfo">mrmrmrmr</span></div></div></div><div id="comment-tools-6280" class="comment-tools"></div><div class="clear"></div><div id="comment-6280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

