+++
type = "question"
title = "reading cesu-8 data in wireshark"
description = '''hi, iv been doing some work with instant messaging application, and i captured a few messages sent, containing emojis. i filtered the capture, and now i have packets that contain (allegedly, by a coworker) only emojis. as i went throu the data, i noticed i see something like (in asci): 0120#########...'''
date = "2017-07-11T01:28:00Z"
lastmod = "2017-07-12T14:15:00Z"
weight = 62657
keywords = [ "decoder", "encoding" ]
aliases = [ "/questions/62657" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [reading cesu-8 data in wireshark](/questions/62657/reading-cesu-8-data-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62657-score" class="post-score" title="current number of votes">0</div><span id="post-62657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi,</p><p>iv been doing some work with instant messaging application, and i captured a few messages sent, containing emojis. i filtered the capture, and now i have packets that contain (allegedly, by a coworker) only emojis. as i went throu the data, i noticed i see something like (in asci):</p><p>0120########################################################..8.</p><p>now, i assume that the ### part is just to fill the length of the message, and the emoji is either at the start or end of the message. i know the data is encoded in CESU-8. what i need is:</p><p><strong>is there a way to read the data encoded in CESU-8?</strong> because using follow TCP-stream shows me a bunch of options, non of them works for me (i have utf-8, which isnt good since im not in the BMP).</p><p>i think what i need is <strong>a lua script that adds a decoder, or maybe any other way to convert the data to UTF-8</strong>, but of course, any help that can be given or suggested will be appreciated.</p><p>thanks, Joseph</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decoder" rel="tag" title="see questions tagged &#39;decoder&#39;">decoder</span> <span class="post-tag tag-link-encoding" rel="tag" title="see questions tagged &#39;encoding&#39;">encoding</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '17, 01:28</strong></p><img src="https://secure.gravatar.com/avatar/928da98430d93815eebe910dd6f021a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="josephg&#39;s gravatar image" /><p><span>josephg</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="josephg has no accepted answers">0%</span></p></div></div><div id="comments-container-62657" class="comments-container"></div><div id="comment-tools-62657" class="comment-tools"></div><div class="clear"></div><div id="comment-62657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62687"></span>

<div id="answer-container-62687" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62687-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62687-score" class="post-score" title="current number of votes">0</div><span id="post-62687-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's currently nothing in Wireshark <em>itself</em> that understands CESU-8, so any dissector you write (in Lua or C) would have to translate it to UTF-8 (the internal character encoding of Wireshark) itself.</p><p>We could add CESU-8 as a character encoding, in which case you could write a dissector (in Lua or C) that used the new encoding to extract a string.</p><p>However, if you don't know the IM application's packet format, you can't just write a working dissector - you'll have to write something that tries its best to dissect what you <em>think</em> is the string, guessing what its length is.</p><p>We could also add CESU-8 support to the Follow TCP Stream dialog; there's no way to add that with a plugin.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '17, 19:07</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-62687" class="comments-container"><span id="62725"></span><div id="comment-62725" class="comment"><div id="post-62725-score" class="comment-score"></div><div class="comment-text"><p>hi, thanks a lot. it makes me a little sad to know that i have to translate the encoding itself, but at least now i know where i stand in that context.</p><p>i will follow to see if there will be any support in the future. both suggestions would be great equally.</p><p>thanks again, joseph</p></div><div id="comment-62725-info" class="comment-info"><span class="comment-age">(12 Jul '17, 13:50)</span> <span class="comment-user userinfo">josephg</span></div></div><span id="62726"></span><div id="comment-62726" class="comment"><div id="post-62726-score" class="comment-score"></div><div class="comment-text"><p>Encodings tend to be added if there's a protocol that uses them (or, in the case of ISO 8859-1, if support can be added by running a program to generate a translation table and then adding a few lines of code).</p><p>There will probably only be CESU-8 support in the future if somebody files an enhancement request on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>, so as to put the request "on the radar screen".</p></div><div id="comment-62726-info" class="comment-info"><span class="comment-age">(12 Jul '17, 13:55)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="62727"></span><div id="comment-62727" class="comment"><div id="post-62727-score" class="comment-score"></div><div class="comment-text"><p>Am I wrong when I understand CESU-8 to be algorithmically translatable into UTF-8 as it in general requires just manipulations of groups of bits?</p></div><div id="comment-62727-info" class="comment-info"><span class="comment-age">(12 Jul '17, 13:58)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="62728"></span><div id="comment-62728" class="comment"><div id="post-62728-score" class="comment-score"></div><div class="comment-text"><p>From <a href="http://www.unicode.org/reports/tr26/">the specification for CESU-8</a>, it appears that</p><pre><code> for (everything in the string) {
    code_point = extract_cesu_8_element();
    if (that failed for any reason, including an octet having the 4 upper bits set)
        fail;
    if (code point introduces a surrogate pair) {
        rest_of_surrogate_pair = extract_cesu_8_element();
        if (that failed for any reason, including an octet having the 4 upper bits set)
            fail;
        if (rest_of_surrogate_pair isn&#39;t the second half of a surrogate pair)
            fail;
        combine code_point and rest_of_surrogate_pair;
        put the resulting Unicode character;
    } else
        put code_point;
}</code></pre><p>where <code>extract_cesu_8_element()</code> is similar to the code to turn a sequence of octets in UTF-8 into a Unicode code point, except that it fails if any octet is of the form 1111xxxx, would generate a UTF-8 string from a valid CESU-8 string (and report an error for an invalid CESU-8 string).</p></div><div id="comment-62728-info" class="comment-info"><span class="comment-age">(12 Jul '17, 14:15)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-62687" class="comment-tools"></div><div class="clear"></div><div id="comment-62687-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

