+++
type = "question"
title = "How to handle exceptions on Linux"
description = '''Tshark handles exceptions/assertion failures on Windows, but on Linux, it will crash on exceptions/assertion failures, how to do?'''
date = "2014-02-11T23:28:00Z"
lastmod = "2014-02-12T17:04:00Z"
weight = 29733
keywords = [ "exception", "crash" ]
aliases = [ "/questions/29733" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to handle exceptions on Linux](/questions/29733/how-to-handle-exceptions-on-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29733-score" class="post-score" title="current number of votes">0</div><span id="post-29733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Tshark handles exceptions/assertion failures on Windows, but on Linux, it will crash on exceptions/assertion failures, how to do?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-exception" rel="tag" title="see questions tagged &#39;exception&#39;">exception</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '14, 23:28</strong></p><img src="https://secure.gravatar.com/avatar/13679628c84abac93be65773340d2589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="metamatrix&#39;s gravatar image" /><p><span>metamatrix</span><br />
<span class="score" title="56 reputation points">56</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="metamatrix has one accepted answer">100%</span></p></div></div><div id="comments-container-29733" class="comments-container"><span id="29734"></span><div id="comment-29734" class="comment"><div id="post-29734-score" class="comment-score"></div><div class="comment-text"><p>can you please show an example where tshark on Windows fails 'in a better/different way' than on Linux?</p></div><div id="comment-29734-info" class="comment-info"><span class="comment-age">(12 Feb '14, 00:39)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29808"></span><div id="comment-29808" class="comment"><div id="post-29808-score" class="comment-score"></div><div class="comment-text"><p>e.g. packet-frame.c ln 491</p><pre><code>        /* Win32: Visual-C Structured Exception Handling (SEH) to trap hardware exceptions
           like memory access violations.
           (a running debugger will be called before the except part below) */
                /* Note: A Windows &quot;exceptional exception&quot; may leave the kazlib&#39;s (Portable Exception Handling)
                   stack in an inconsistent state thus causing a crash at some point in the
                   handling of the exception.*/
    TRY {
#ifdef _MSC_VER
        __try {
#endif

    ...

#ifdef _MSC_VER
        }
#endif

#ifdef _MSC_VER
        } __except(EXCEPTION_EXECUTE_HANDLER /* handle all exceptions */) {
            switch(GetExceptionCode()) {
            case(STATUS_ACCESS_VIOLATION):
                show_exception(tvb, pinfo, parent_tree, DissectorError,
                           &quot;STATUS_ACCESS_VIOLATION: dissector accessed an invalid memory address&quot;);
                break;
            case(STATUS_INTEGER_DIVIDE_BY_ZERO):
                show_exception(tvb, pinfo, parent_tree, DissectorError,
                           &quot;STATUS_INTEGER_DIVIDE_BY_ZERO: dissector tried an integer division by zero&quot;);
                break;
            case(STATUS_STACK_OVERFLOW):
                show_exception(tvb, pinfo, parent_tree, DissectorError,
                           &quot;STATUS_STACK_OVERFLOW: dissector overflowed the stack (e.g. endless loop)&quot;);
                /* XXX - this will have probably corrupted the stack,
                   which makes problems later in the exception code */
                break;
                /* XXX - add other hardware exception codes as required */
            default:
                show_exception(tvb, pinfo, parent_tree, DissectorError,
                           g_strdup_printf(&quot;dissector caused an unknown exception: 0x%x&quot;, GetExceptionCode()));
            }
        }
#endif</code></pre></div><div id="comment-29808-info" class="comment-info"><span class="comment-age">(12 Feb '14, 17:02)</span> <span class="comment-user userinfo">metamatrix</span></div></div><span id="29809"></span><div id="comment-29809" class="comment"><div id="post-29809-score" class="comment-score"></div><div class="comment-text"><p>What are you trying to do on Linux with tshark?</p></div><div id="comment-29809-info" class="comment-info"><span class="comment-age">(12 Feb '14, 17:04)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-29733" class="comment-tools"></div><div class="clear"></div><div id="comment-29733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29805"></span>

<div id="answer-container-29805" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29805-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29805-score" class="post-score" title="current number of votes">0</div><span id="post-29805-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="metamatrix has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You'd have to catch SIGSEGV, SIGBUS, SIGFPE (which, in practice, many UN*Xes use for integer division), and SIGABRT (which is what <code>abort()</code> delivers; that's what tends to be used for at least some assertions) in, for example, <code>dissect_frame()</code> in <code>epan/dissectors/packet-frame.c</code> and, in the handler, somehow manage to handle those conditions.</p><p>UN*X systems don't have Windows-style structured exception handling for errors such as those, so that's going to be harder to do.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '14, 16:52</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Feb '14, 01:20</strong> </span></p></div></div><div id="comments-container-29805" class="comments-container"></div><div id="comment-tools-29805" class="comment-tools"></div><div class="clear"></div><div id="comment-29805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

