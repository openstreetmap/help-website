+++
type = "question"
title = "proto_tree_append_text function"
description = '''Hello, I am writing a dissector in C and I donwloaded the last version of the source from svn. I want to use the proto_tree_append_text to add a label to an item. My compiler said that this function is not defined. This are are my include at the begin of my c file: #ifdef HAVE_CONFIG_H # include &quot;co...'''
date = "2010-12-17T05:39:00Z"
lastmod = "2010-12-17T07:17:00Z"
weight = 1380
keywords = [ "include", "proto_tree_add" ]
aliases = [ "/questions/1380" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [proto\_tree\_append\_text function](/questions/1380/proto_tree_append_text-function)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1380-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am writing a dissector in C and I donwloaded the last version of the source from svn. I want to use the proto_tree_append_text to add a label to an item. My compiler said that this function is not defined. This are are my include at the begin of my c file:</p><pre><code>#ifdef HAVE_CONFIG_H
# include &quot;config.h&quot;

#endif

#include &lt;stdio.h&gt;
#include &lt;glib.h&gt;
#include &lt;epan/packet.h&gt;
#include &lt;epan/emem.h&gt;
#include &lt;epan/dissectors/packet-tcp.h&gt;
#include &lt;epan/prefs.h&gt;
#include &lt;string.h&gt;</code></pre><p>Somebody can help me and tell what include I should add?</p><p>Thanks. Sandrine.</p></div><div id="question-tags" class="tags-container tags">include proto_tree_add</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '10, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/a141a084e9ce66ec32b7f064776798bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sandrine%20Beauche&#39;s gravatar image" /><p>Sandrine Bea...<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sandrine Beauche has no accepted answers">0%</span></p></div></div><div id="comments-container-1380" class="comments-container"></div><div id="comment-tools-1380" class="comment-tools"></div><div class="clear"></div><div id="comment-1380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1381"></span>

<div id="answer-container-1381" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1381-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The function to use would be proto_item_append_text and is declared in epan/proto.h:</p><pre><code>/** Append to text of item after it has already been created.
 @param ti the item to append the text to
 @param format printf like format string
 @param ... printf like parameters */
extern void proto_item_append_text(proto_item *ti, const char *format, ...)
        G_GNUC_PRINTF(2,3);</code></pre><p>Hope this helps :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '10, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1381" class="comments-container"></div><div id="comment-tools-1381" class="comment-tools"></div><div class="clear"></div><div id="comment-1381-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

