+++
type = "question"
title = "Show address resolution usage"
description = '''Hello, I am in middle of troubleshooting the issue and have noticed couple of things. I have network name resolution checked for MAC and Network layer, sniffer traces does show name resolution during live captures however, as soon as file is saved and re-opened some entries are missing. So, I have c...'''
date = "2013-07-03T01:08:00Z"
lastmod = "2013-07-03T01:08:00Z"
weight = 22588
keywords = [ "wireshark" ]
aliases = [ "/questions/22588" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Show address resolution usage](/questions/22588/show-address-resolution-usage)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22588-score" class="post-score" title="current number of votes">0</div><span id="post-22588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am in middle of troubleshooting the issue and have noticed couple of things.</p><p>I have network name resolution checked for MAC and Network layer, sniffer traces does show name resolution during live captures however, as soon as file is saved and re-opened some entries are missing. So, I have couple of queries :-</p><ol><li><p>Does Name Resolution looks at the current workstation cache and if TTL is small the cache will be deleted so, we don't see the mapping later on? - THIS IS JUST GUESS i could not locate any instance from source code. If this is the case, do we have a Enhancement/feature request to save cache in .pcap file as snapshot to maintain consistency in checking saved sniffer traces.</p></li><li><p>Why there is a difference values shown in Statistics =&gt; <em>'Show name resolution'</em> during live capture and same captures reopened in exact same PC and in different PC.</p></li><li><p>I can see we have an option to Click "OK" for 'Show name resolution' and it does let us enter text however "OK" button does not seems to be working ( it lets us in same screem). Is this a defect? I am using version 1.10.0 (SVN Rev 49790 from /trunk-1.10). I could not find one in bugzilla.</p></li><li><p>We have an option for Manually Resolve Name under View =&gt; Name Resolution =&gt; Manually Resolve Name. However, the value defined is not resolving the name. Is this a know issue as specified in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8462">8462</a> which shows status as Unconfirmed?. What does status Unconfirmed means and do we have a workaround for this? I can see a host file workaround listed; however, modifying entry for hosts.txt did not worked for me.</p></li></ol><p>Regards,</p><p>-Deepak</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '13, 01:08</strong></p><img src="https://secure.gravatar.com/avatar/a8aa1b50bd4e70fe64d8c9612d100eb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Deepak&#39;s gravatar image" /><p><span>Deepak</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Deepak has one accepted answer">25%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Jul '13, 23:49</strong> </span></p></div></div><div id="comments-container-22588" class="comments-container"></div><div id="comment-tools-22588" class="comment-tools"></div><div class="clear"></div><div id="comment-22588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

