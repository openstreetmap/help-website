+++
type = "question"
title = "command of tshark can not support Chinese path or Chinese file name"
description = '''tshark` fails if its parameters contain Chinese characters (in a path parameter). For example: tshark -r d:&#92;中文.pcap -V -T text &amp;gt; d:&#92;1.txt  wireshark 1.5.1 has solved the problem. but how to correct the source code if i just want to use wireshark1.2.9 ? which code of wireshark1.2.9 should be modif...'''
date = "2011-09-15T19:20:00Z"
lastmod = "2011-09-18T20:19:00Z"
weight = 6407
keywords = [ "tshark", "unicode", "error" ]
aliases = [ "/questions/6407" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [command of tshark can not support Chinese path or Chinese file name](/questions/6407/command-of-tshark-can-not-support-chinese-path-or-chinese-file-name)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6407-score" class="post-score" title="current number of votes">0</div><span id="post-6407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>tshark` fails if its parameters contain Chinese characters (in a path parameter). For example:</p><pre><code>tshark -r d:\中文.pcap -V -T text &gt; d:\1.txt</code></pre><p>wireshark 1.5.1 has solved the problem. but how to correct the source code if i just want to use wireshark1.2.9 ? which code of wireshark1.2.9 should be modified in order to solve the problem.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-unicode" rel="tag" title="see questions tagged &#39;unicode&#39;">unicode</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '11, 19:20</strong></p><img src="https://secure.gravatar.com/avatar/a5a3214300b3b17fc46c3b656b7bed01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ylda_ljm0620&#39;s gravatar image" /><p><span>ylda_ljm0620</span><br />
<span class="score" title="31 reputation points">31</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ylda_ljm0620 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Sep '11, 23:49</strong> </span></p></div></div><div id="comments-container-6407" class="comments-container"></div><div id="comment-tools-6407" class="comment-tools"></div><div class="clear"></div><div id="comment-6407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6428"></span>

<div id="answer-container-6428" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6428-score" class="post-score" title="current number of votes">1</div><span id="post-6428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://msdn.microsoft.com/en-us/library/bb776391%28v=vs.85%29.aspx">CommandLineToArgvW</a> requires shell32.lib. You probably just need to make <a href="http://anonsvn.wireshark.org/viewvc/trunk/Makefile.nmake?r1=35411&amp;r2=35410&amp;pathrev=35411">this</a> change to Makefile.nmake. In fact, you may want to apply all the changes committed in <a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=35411">r35411</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '11, 14:14</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Sep '11, 14:17</strong> </span></p></div></div><div id="comments-container-6428" class="comments-container"><span id="6412"></span><div id="comment-6412" class="comment"><div id="post-6412-score" class="comment-score"></div><div class="comment-text"><p>to solve the problem, i modified in tshark.c of wireshark1.2.9 as follow:</p><pre><code>int
main(int argc, char *argv[])
{
  char                *init_progfile_dir_error;
  int                  opt, i;
  extern char         *optarg;
  gboolean             arg_error = FALSE;

#ifdef _WIN32
  WSADATA       wsaData;
  LPWSTR              *wc_argv;
  int                  wc_argc,j;
#endif  /* _WIN32 */

...

  static const char    optstring[] = OPTSTRING_INIT OPTSTRING_WIN32;

#ifdef _WIN32
  /* Convert our arg list to UTF-8. */
  wc_argv = CommandLineToArgvW(GetCommandLineW(), &amp;wc_argc);
  if (wc_argv &amp;&amp; wc_argc == argc) {
    for (j = 0; j &lt; argc; j++) {
      argv[j] = g_utf16_to_utf8(wc_argv[j], -1, NULL, NULL, NULL);
    }
  } /* XXX else bail because something is horribly, horribly wrong? */
#endif /* _WIN32 */

...</code></pre><p>but i can not compile successfully. the error ：</p><pre><code>tshark.c
tshark.c(772) : error C2220: warning treated as error - no &#39;object&#39; file generat
ed
tshark.c(772) : warning C4013: &#39;CommandLineToArgvW&#39; undefined; assuming extern r
eturning int
tshark.c(772) : warning C4047: &#39;=&#39; : &#39;LPWSTR *&#39; differs in levels of indirection
 from &#39;int&#39;
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN
\cl.EXE&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre><p>how should i modify the thark.c？</p></div><div id="comment-6412-info" class="comment-info"><span class="comment-age">(16 Sep '11, 02:10)</span> <span class="comment-user userinfo">ylda_ljm0620</span></div></div><span id="6441"></span><div id="comment-6441" class="comment"><div id="post-6441-score" class="comment-score"></div><div class="comment-text"><p>thanks. It success.</p><p>i add shell32.lib to tshark_LIBS in Makefile.nmake, add #include &lt;shellapi.h&gt; in tshark.c.</p></div><div id="comment-6441-info" class="comment-info"><span class="comment-age">(18 Sep '11, 20:19)</span> <span class="comment-user userinfo">ylda_ljm0620</span></div></div></div><div id="comment-tools-6428" class="comment-tools"></div><div class="clear"></div><div id="comment-6428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

