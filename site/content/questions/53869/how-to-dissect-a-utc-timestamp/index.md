+++
type = "question"
title = "How to dissect a UTC timestamp"
description = '''I am trying to write a customized dissector as a plugin on windows platform.  I am doing this on version 2.1.1-git, win32.  Details of the data: It is a UTC Timestamp. The number of nanoseconds since January 1, 1970, 00:00:00 GMT, precision is provided to the nearest millsecond. The format of this f...'''
date = "2016-07-06T19:00:00Z"
lastmod = "2016-07-07T02:47:00Z"
weight = 53869
keywords = [ "dissector" ]
aliases = [ "/questions/53869" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to dissect a UTC timestamp](/questions/53869/how-to-dissect-a-utc-timestamp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53869-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53869-score" class="post-score" title="current number of votes">0</div><span id="post-53869-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to write a customized dissector as a plugin on windows platform.<br />
<br />
I am doing this on version 2.1.1-git, win32.<br />
<br />
Details of the data:<br />
It is a UTC Timestamp. The number of nanoseconds since January 1, 1970, 00:00:00 GMT, precision is provided to the nearest millsecond.<br />
The format of this field is Uint64.<br />
<br />
I have the following code to dissect a UTC time stamp with 64 bit, in little endian:<br />
</p><pre><code>void 
proto_register_foo(void) {
    static hf_register_info hf[] = {
        { &amp;hf_foo_send_time, { &quot;FOO SendTime&quot;, &quot;foo.sendtime&quot;, FT_ABSOBUTE_TIME, ABSOLUTE_TIME_UTC, NULL, 0x0, NULL, HFILL }}
    };
    ... 
}

static int
dissect_foo(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree _U_, void *data _U_)
{
...
proto_tree_add_item(omdd_tree, hg_omdd_send_time, tvb, 0, 8, ENC_LITTLE_ENDIAN);
...
}</code></pre><p>The problem is the result is not correct. Does anyone know how to dissect a UTC time stamp?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '16, 19:00</strong></p><img src="https://secure.gravatar.com/avatar/7c0faeca14601a7e181f27988b503982?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SulfredLee&#39;s gravatar image" /><p><span>SulfredLee</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SulfredLee has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jul '16, 22:28</strong> </span></p></div></div><div id="comments-container-53869" class="comments-container"><span id="53871"></span><div id="comment-53871" class="comment"><div id="post-53871-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "a UTC time stamp"? What are the units of the time stamp? Seconds? Fractions of a second? If it's fractions of a second, what fraction - microseconds, nanoseconds, other? Is the time stamp a count of fractions of a second, or seconds, since some point in time? If so, what is that point in time? Is it, for example, January 1, 1970, 00:00:00 UTC? Or is it, for example, a 32-bit count of seconds since some point in time and a 32-bit count of fractions of a second since the second in question? Without knowing that, nobody can know how to dissect it.</p></div><div id="comment-53871-info" class="comment-info"><span class="comment-age">(06 Jul '16, 20:49)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="53872"></span><div id="comment-53872" class="comment"><div id="post-53872-score" class="comment-score"></div><div class="comment-text"><p>Sorry for leak of information.<br />
I got the description from the development guide is that:<br />
It is a UTC Timestamp. The number of nanoseconds since January 1, 1970, 00:00:00 GMT, precision is provided to the nearest millsecond.<br />
The format of this field is Uint64.</p></div><div id="comment-53872-info" class="comment-info"><span class="comment-age">(06 Jul '16, 20:53)</span> <span class="comment-user userinfo">SulfredLee</span></div></div></div><div id="comment-tools-53869" class="comment-tools"></div><div class="clear"></div><div id="comment-53869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53879"></span>

<div id="answer-container-53879" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53879-score" class="post-score" title="current number of votes">2</div><span id="post-53879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SulfredLee has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, there is currently no ENC_ value for that time stamp format, so you would have to do it manually:</p><pre><code>guint64 timestamp;
nstime_t ts_nstime;

    ...

timestamp = tvb_get_letoh64(tvb, 0, 8);
ts_nstime.secs = timestamp / 1000000000;
ts.nstime_nsecs = timestamp % 1000000000;
proto_tree_add_time(omdd_tree, hg_omdd_send_time, tvb, 0, 8, &amp;ts_nstime);</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '16, 00:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div></div><div id="comments-container-53879" class="comments-container"><span id="53883"></span><div id="comment-53883" class="comment"><div id="post-53883-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much, it works.</p></div><div id="comment-53883-info" class="comment-info"><span class="comment-age">(07 Jul '16, 01:17)</span> <span class="comment-user userinfo">SulfredLee</span></div></div><span id="53885"></span><div id="comment-53885" class="comment"><div id="post-53885-score" class="comment-score"></div><div class="comment-text"><p>Sorry, one more question. I have already get the value to ts_nstime. Why I still have to use the data in tvb at the api <code>proto_tree_add_time</code> ?</p></div><div id="comment-53885-info" class="comment-info"><span class="comment-age">(07 Jul '16, 01:54)</span> <span class="comment-user userinfo">SulfredLee</span></div></div><span id="53887"></span><div id="comment-53887" class="comment"><div id="post-53887-score" class="comment-score"></div><div class="comment-text"><p>Because you want the value of the field to be in the protocol tree, and fetching the value from the packet and converting it to a nstime_t doesn't put it into the protocol tree - only a <code>proto_tree_add_</code> call can do that.</p></div><div id="comment-53887-info" class="comment-info"><span class="comment-age">(07 Jul '16, 02:08)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="53888"></span><div id="comment-53888" class="comment"><div id="post-53888-score" class="comment-score"></div><div class="comment-text"><p>Here is my understanding, when I put <code>&amp;ts_nstime</code> into <code>proto_tree_add_time</code>, this api will ignore the present of <code>tvb, 0, 8</code>, am I correct @@?</p></div><div id="comment-53888-info" class="comment-info"><span class="comment-age">(07 Jul '16, 02:15)</span> <span class="comment-user userinfo">SulfredLee</span></div></div><span id="53889"></span><div id="comment-53889" class="comment"><div id="post-53889-score" class="comment-score">1</div><div class="comment-text"><p>No, you are not correct. It will not <em>fetch the data</em> from the tvbuff, but it will <em>record</em> that the data came from the tvbuff, starting at an offset of 0, for 8 bytes, so that, for example, if you click on on the item in the protocol details pane it will highlight the corresponding data in the hex dump pane.</p></div><div id="comment-53889-info" class="comment-info"><span class="comment-age">(07 Jul '16, 02:47)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-53879" class="comment-tools"></div><div class="clear"></div><div id="comment-53879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

