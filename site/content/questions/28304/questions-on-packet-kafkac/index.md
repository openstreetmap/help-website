+++
type = "question"
title = "Questions on packet-kafka.c"
description = '''Hello,  I have some observations on packet-kafka.c, that  do not look correct to me. Can somebody comment on them ? (I am very new to this so please forgive me if this question is trivial).  1) No attempt to call proto_item_add_subtree(ti, ett_kafka_metadata_topics);   yet &quot;ett_kafka_metadata_topics...'''
date = "2013-12-20T04:09:00Z"
lastmod = "2013-12-20T06:31:00Z"
weight = 28304
keywords = [ "kafka" ]
aliases = [ "/questions/28304" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Questions on packet-kafka.c](/questions/28304/questions-on-packet-kafkac)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28304-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have some observations on packet-kafka.c, that do not look correct to me. Can somebody comment on them ? (I am very new to this so please forgive me if this question is trivial).</p><pre><code>1) No attempt to call proto_item_add_subtree(ti, ett_kafka_metadata_topics); 
     yet &quot;ett_kafka_metadata_topics&quot; is contained in an array that is passed to 
     proto_register_subtree_array(..);

2) There are multiple invocations of the following where the second argument
     is not unique. Is this a problem ?

     subtree = proto_item_add_subtree(ti, ett_kafka_request_partition);
     subtree = proto_item_add_subtree(ti, ett_kafka_request_topic);
     subtree = proto_item_add_subtree(ti, ett_kafka_response_partition);
     subtree = proto_item_add_subtree(ti, ett_kafka_response_topic);</code></pre></div><div id="question-tags" class="tags-container tags">kafka</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '13, 04:09</strong></p><img src="https://secure.gravatar.com/avatar/93d686d9896fc2009387e5f0185612f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gahanr&#39;s gravatar image" /><p>gahanr<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gahanr has no accepted answers">0%</span></p></div></div><div id="comments-container-28304" class="comments-container"></div><div id="comment-tools-28304" class="comment-tools"></div><div class="clear"></div><div id="comment-28304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28305"></span>

<div id="answer-container-28305" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28305-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Yes, that appears to have been a cut-n-pasteo. It is now fixed (r54294).</li><li>No, that's not necessarily a problem. It just means that there are multiple places in the decode tree which will be expanded or collapsed based on the same ett_ variable. It's a style thing but not a problem.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Dec '13, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-28305" class="comments-container"><span id="28306"></span><div id="comment-28306" class="comment"><div id="post-28306-score" class="comment-score"></div><div class="comment-text"><p>ett_kafka_metadata_topics is already used in dissect_kafka_metadata_response(). The tree in dissect_kafka_metadata_request() <em>was</em> a cut-n-pasteo, but I should have just removed it completely (r54301).</p></div><div id="comment-28306-info" class="comment-info"><span class="comment-age">(20 Dec '13, 07:05)</span> eapache</div></div></div><div id="comment-tools-28305" class="comment-tools"></div><div class="clear"></div><div id="comment-28305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

