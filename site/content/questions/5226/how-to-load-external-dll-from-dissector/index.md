+++
type = "question"
title = "How to Load External DLL from Dissector"
description = '''I have a DLL file named, Test2.dll which loads fine in anything but wireshark, but when I try to open it within my wireshark dissector it fails to load, this is how I am loading it: #define LIBRARYLOCATION &quot;C:&#92;&#92;Docum...&#92;&#92;Test2.dll&quot;  ...  static void dissect_foo(tvbuff_t *tvb, packet_info *pinfo, pro...'''
date = "2011-07-25T11:56:00Z"
lastmod = "2011-07-25T17:55:00Z"
weight = 5226
keywords = [ "dissector", "dll" ]
aliases = [ "/questions/5226" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to Load External DLL from Dissector](/questions/5226/how-to-load-external-dll-from-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5226-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a DLL file named, Test2.dll which loads fine in anything but wireshark, but when I try to open it within my wireshark dissector it fails to load, this is how I am loading it:</p><pre><code>#define LIBRARYLOCATION &quot;C:\\Docum...\\Test2.dll&quot;

...

static void dissect_foo(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree){
HINSTANCE DLLInstance = LoadLibrary((LPCWSTR)LIBRARYLOCATION);

if(DLLInstance == NULL){
proto_tree_add_text(tree, NULL, 0, 0, &quot;Cannot Load DLL: %*s&quot;, 0, LIBRARYLOCATION);}
else{
proto_tree_add_text(tree, NULL, 0, 0, &quot;Loaded DLL: %*s&quot;, 0, LIBRARYLOCATION);}</code></pre><p>The .h file for the DLL is thus:</p><pre><code>#ifndef TEST2_H
#define TEST2_H

#ifdef __cplusplus

extern &quot;C&quot;
{
#endif
__declspec(dllexport) void Foo ();
#ifdef __cplusplus
}
#endif
#endif</code></pre><p>Any ideas as to why this wouldn't work? The DLL is compiled in VC++ 2005 (No option there) and the dissector is compiled with VC++ 2010 EE.</p><p>Thank you for your time, Brandon</p></div><div id="question-tags" class="tags-container tags">dissector dll</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '11, 11:56</strong></p><img src="https://secure.gravatar.com/avatar/b65eb296474b8a4c664c8f7bc0ba2234?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="officialhopsof&#39;s gravatar image" /><p>officialhopsof<br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="officialhopsof has 2 accepted answers">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jul '11, 17:57</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5226" class="comments-container"><span id="5231"></span><div id="comment-5231" class="comment"><div id="post-5231-score" class="comment-score"></div><div class="comment-text"><p>What is the error returned from the LoadLibrary call? To get extended error info call GetLastError() as per the <a href="http://msdn.microsoft.com/en-us/library/ms684175%28v=vs.85%29.aspx">MSDN</a> page for LoadLibrary.</p></div><div id="comment-5231-info" class="comment-info"><span class="comment-age">(25 Jul '11, 13:24)</span> grahamb ♦</div></div><span id="5234"></span><div id="comment-5234" class="comment"><div id="post-5234-score" class="comment-score"></div><div class="comment-text"><p>ERROR_MOD_NOT_FOUND<br />
126 (0x7E)<br />
<br />
<br />
is the error I get, so this points to a path issue? Is that possible since I am using an absolute path?</p></div><div id="comment-5234-info" class="comment-info"><span class="comment-age">(25 Jul '11, 14:16)</span> officialhopsof</div></div></div><div id="comment-tools-5226" class="comment-tools"></div><div class="clear"></div><div id="comment-5226-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5238"></span>

<div id="answer-container-5238" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5238-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><strong>Bug:</strong> You're passing a single-char string as a wide-char string to <a href="http://msdn.microsoft.com/en-us/library/ms684175(v=vs.85).aspx"><code>LoadLibrary</code></a>, but you actually need to pass in a <code>TCHAR</code> string (which is set at compile-time to be either wide-char or single-char).</p><p><strong>Fix:</strong> Use <a href="http://social.msdn.microsoft.com/Forums/en/vcgeneral/thread/8ce6ddef-3f1a-4033-a28b-54af91766e9f"><code>_T</code></a> for the literal <code>#define</code>, and remove the <code>LPCWSTR</code> cast (presumably done to mute the compiler warning you should've heeded).</p><p>from:</p><pre><code>#define LIBRARYLOCATION &quot;C:\\Docum...\\Test2.dll&quot;
/* ... */
HINSTANCE DLLInstance = LoadLibrary((LPCWSTR)LIBRARYLOCATION);</code></pre><p>to:</p><pre><code>//#include &lt;tchar.h&gt;
#define LIBRARYLOCATION _T(&quot;C:\\Docum...\\Test2.dll&quot;)
/* ... */
HINSTANCE DLLInstance = LoadLibrary(LIBRARYLOCATION);</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '11, 17:55</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span> </br></br></p></div></div><div id="comments-container-5238" class="comments-container"><span id="5259"></span><div id="comment-5259" class="comment"><div id="post-5259-score" class="comment-score"></div><div class="comment-text"><p>That did the trick! I also really liked how you included the example!</p><p>Thanks! Brandon</p></div><div id="comment-5259-info" class="comment-info"><span class="comment-age">(26 Jul '11, 07:06)</span> officialhopsof</div></div><span id="5265"></span><div id="comment-5265" class="comment"><div id="post-5265-score" class="comment-score"></div><div class="comment-text"><p>Good spot, I missed the cast.</p><p>More portably you could define the string literal as a wide character e.g. L"\path\to\your\dll".</p><p>No need to use Windows generic types then.</p></div><div id="comment-5265-info" class="comment-info"><span class="comment-age">(26 Jul '11, 10:00)</span> grahamb ♦</div></div><span id="5271"></span><div id="comment-5271" class="comment"><div id="post-5271-score" class="comment-score"></div><div class="comment-text"><p>Using <code>L</code> would cause the same problem if <code>UNICODE</code> was not defined (in which case <code>LoadLibrary</code> expects a single-char string instead). If portability were a goal, I would use <a href="http://developer.gnome.org/glib/unstable/glib-Dynamic-Loading-of-Modules.html">GLib's dynamic module loading</a> (designed to be cross-platform).</p></div><div id="comment-5271-info" class="comment-info"><span class="comment-age">(26 Jul '11, 11:24)</span> bstn</div></div></div><div id="comment-tools-5238" class="comment-tools"></div><div class="clear"></div><div id="comment-5238-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

