+++
type = "question"
title = "[closed] Why SQL batch is slow"
description = '''The problem is I&#x27;m seeing a 22 second delay coming from the pc on a sql batch. I trying to find out what is causing the delay and I know you supposely was you spot the delay you look what is happening before your frame # to see why it is delayed. My question is if the captured is interwined with out...'''
date = "2016-06-29T09:31:00Z"
lastmod = "2016-06-29T09:31:00Z"
weight = 53731
keywords = [ "stream", "tcp", "sql" ]
aliases = [ "/questions/53731" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Why SQL batch is slow](/questions/53731/why-sql-batch-is-slow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53731-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The problem is I'm seeing a 22 second delay coming from the pc on a sql batch. I trying to find out what is causing the delay and I know you supposely was you spot the delay you look what is happening before your frame # to see why it is delayed. My question is if the captured is interwined with out conversation do you just resort the no column and what ever frame number shows the delay you look above that to see what was going on like the picture below:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/different_streams.png" alt="alt text" /></p><p>or should filtered on that stream where the delay is to determine what is causing the delay like the picture below:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/tcpstream_VitXcQV.png" alt="alt text" /></p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">stream tcp sql</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '16, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/1ace388d473a7dc2c6ffb774562b02ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patrickwill&#39;s gravatar image" /><p>patrickwill<br />
<span class="score" title="0 reputation points">0</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patrickwill has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>closed 01 Jul '16, 07:14</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></img></div></div><div id="comments-container-53731" class="comments-container"><span id="53735"></span><div id="comment-53735" class="comment"><div id="post-53735-score" class="comment-score"></div><div class="comment-text"><p>just out of curiosity, is SQL running on a VM or physical machine?</p></div><div id="comment-53735-info" class="comment-info"><span class="comment-age">(29 Jun '16, 13:08)</span> net_tech</div></div><span id="53737"></span><div id="comment-53737" class="comment"><div id="post-53737-score" class="comment-score"></div><div class="comment-text"><p>it is a vm machine</p></div><div id="comment-53737-info" class="comment-info"><span class="comment-age">(29 Jun '16, 15:40)</span> patrickwill</div></div><span id="53739"></span><div id="comment-53739" class="comment"><div id="post-53739-score" class="comment-score"></div><div class="comment-text"><p>the bug described in the KB below would be responsible for sql performance degradation, but not 22 seconds delay you mentioned in your post.</p><p>it also would be helpful if you describe your environment, so we don't have to guess.<br />
</p><p><a href="https://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=2129176">https://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=2129176</a></p><p>the delay could be caused by insufficient memory, slow disk or cpu. have you looked at the perfmon values?</p></div><div id="comment-53739-info" class="comment-info"><span class="comment-age">(29 Jun '16, 18:07)</span> net_tech</div></div></div><div id="comment-tools-53731" class="comment-tools"></div><div class="clear"></div><div id="comment-53731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question - A 2nd question was opened for this; closing this one as a duplicate since the other one has a capture file. https://ask.wireshark.org/questions/53703/slow-performance-on-aveva-software" by JeffMorriss 01 Jul '16, 07:14

</div>

</div>

</div>

