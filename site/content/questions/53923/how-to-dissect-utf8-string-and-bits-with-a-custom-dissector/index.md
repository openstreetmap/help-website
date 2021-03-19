+++
type = "question"
title = "How to dissect UTF8 string and bits with a custom dissector"
description = '''I am trying to write a customized dissector as a plugin on windows platform. I am doing this on version 2.1.1-git, win32.  Q1 I have a string which has 320 length, Unicode UTF-16LE encoded. I am trying to do the following parsing but the result is I can only get the first char on the front end displ...'''
date = "2016-07-07T20:32:00Z"
lastmod = "2016-07-07T21:41:00Z"
weight = 53923
keywords = [ "dissector" ]
aliases = [ "/questions/53923" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to dissect UTF8 string and bits with a custom dissector](/questions/53923/how-to-dissect-utf8-string-and-bits-with-a-custom-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53923-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to write a customized dissector as a plugin on windows platform.<br />
I am doing this on version 2.1.1-git, win32.<br />
<br />
<strong>Q1</strong><br />
I have a string which has 320 length, Unicode UTF-16LE encoded. I am trying to do the following parsing but the result is I can only get the first char on the front end display.<br />
For example, I received a string "Hello Lee", after I do my parsing, I can only see "H" in the front end.<br />
I have the following related code.<br />
</p><pre><code>void
proto_register_foo(void)
{
    //...
    static hf_register_int hf[] = {
        { &amp;hf_foo_message, { &quot;Message&quot;, &quot;foo.message&quot;, FT_STRING, STR_UNICODE, NULL, 0x0, NULL, HFILL } }
    };
    //...
}

static int
dissect_foo(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree _U_, void *data _U_)
{
    //...
    proto_tree_add_item(foo_tree, hf_foo_message, tvb, 0, 320, ENC_LITTLE_ENDIAN);
    //...
}</code></pre><p>I also tried to get the string from tvb first like this:<br />
</p><pre><code>GByteArray temp_str;
temp_str.data = malloc(320);
temp_str.len = 320;
tvb_get_string_bytes(tvb, *offset, 320, STR_UNICODE, &amp;temp_str, endoff)
calfreeloc(temp_str.data);
temp_str.len = 0;</code></pre><p>but I am not sure how to set the variable <code>endoff</code><br />
</p><p><strong>Q2</strong><br />
I have a byte that include three variables.<br />
bit 1-2 is value_a<br />
bit 3-6 is value_b<br />
bit 7-8 is value_c<br />
<br />
I am trying to do put them into <code>static hf_register_info hf[]</code>, but then I found nothing similar to <code>FT_BITS</code>, what should I do?<br />
</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '16, 20:32</strong></p><img src="https://secure.gravatar.com/avatar/7c0faeca14601a7e181f27988b503982?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SulfredLee&#39;s gravatar image" /><p>SulfredLee<br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SulfredLee has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-53923" class="comments-container"></div><div id="comment-tools-53923" class="comment-tools"></div><div class="clear"></div><div id="comment-53923-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53924"></span>

<div id="answer-container-53924" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53924-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Separate questions should be asked separately, but:</p><p><strong>Q1</strong></p><blockquote><p>Unicode UTF-16LE encoded</p></blockquote><p>...</p><blockquote><pre><code>proto_tree_add_item(foo_tree, hf_foo_message, tvb, 0, 320, ENC_LITTLE_ENDIAN);</code></pre></blockquote><p>You need to specify the full encoding, not just the byte order. for string values. In this case, it's <code>ENC_UTF_16|ENC_LITTLE_ENDIAN</code>, so</p><pre><code> proto_tree_add_item(foo_tree, hf_foo_message, tvb, 0, 320, ENC_UTF_16|ENC_LITTLE_ENDIAN);</code></pre><blockquote><p>I also tried to get the string from tvb first like this:</p></blockquote><p>Try it like this:</p><pre><code>string = tvb_get_string_enc(NULL, tvb, *offset, 320, ENC_UTF_16|ENC_LITTLE_ENDIAN);</code></pre><p>That will return a UTF-8 string that must be freed with <code>g_free()</code>. If you want the <em>raw bytes</em> of the string, do</p><pre><code>buffer = tvb_memdup(NULL, tvb, *offset, 320);</code></pre><p>That will return an array of octets (<em>not</em> null-terminated) that must be freed with <code>g_free()</code>.</p><p><strong>Q2</strong></p><blockquote><p>what should I do?</p></blockquote><p>Define three fields in the <code>hf[]</code> array, and set the <code>bitmask</code> fields of their definitions to be bit masks corresponding to the bits (I don't know whether you're numbering the bits from top to bottom, or from bottom to top, so I don't know what the right masks would be).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '16, 21:41</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div></div><div id="comments-container-53924" class="comments-container"><span id="53925"></span><div id="comment-53925" class="comment"><div id="post-53925-score" class="comment-score"></div><div class="comment-text"><p>Thank you I will try it @@"</p></div><div id="comment-53925-info" class="comment-info"><span class="comment-age">(07 Jul '16, 22:25)</span> SulfredLee</div></div></div><div id="comment-tools-53924" class="comment-tools"></div><div class="clear"></div><div id="comment-53924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

