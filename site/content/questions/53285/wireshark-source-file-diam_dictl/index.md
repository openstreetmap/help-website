+++
type = "question"
title = "wireshark source file diam_dict.l"
description = '''In the source file of Wireshark, in the file &quot;diam_dict.l&quot; (parser for diameter protocol dictionary), I found the following function:   void ddict_free(ddict_t* d) {  ddict_application_t *p, *pn;  ddict_vendor_t *v, *vn;  ddict_cmd_t *c, *cn;  ddict_typedefn_t *t, *tn;  ddict_avp_t *a, *an;  #define...'''
date = "2016-06-07T08:47:00Z"
lastmod = "2016-06-07T12:55:00Z"
weight = 53285
keywords = [ "diameter", "source-code" ]
aliases = [ "/questions/53285" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [wireshark source file diam\_dict.l](/questions/53285/wireshark-source-file-diam_dictl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53285-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In the source file of Wireshark, in the file "diam_dict.l" (parser for diameter protocol dictionary), I found the following function:<br />
</p><pre><code>void
ddict_free(ddict_t* d)
{
    ddict_application_t *p, *pn;
    ddict_vendor_t *v, *vn;
    ddict_cmd_t *c, *cn;
    ddict_typedefn_t *t, *tn;
    ddict_avp_t *a, *an;

#define FREE_NAMEANDOBJ(n) do { if(n-&gt;name) g_free(n-&gt;name); g_free(n); } while(0)

    for (p = d-&gt;applications; p; p = pn ) {
        pn = p-&gt;next;
        FREE_NAMEANDOBJ(p);
    }

    for (v = d-&gt;vendors; v; v = vn) {
        vn = v-&gt;next;
        if (!v-&gt;desc)  g_free(v-&gt;desc);
        FREE_NAMEANDOBJ(v);
    }

    for (c = d-&gt;cmds; c; c = cn ) {
        cn = c-&gt;next;
        FREE_NAMEANDOBJ(c);
    }

    for (t = d-&gt;typedefns; t; t = tn) {
        tn = t-&gt;next;
        if (!t-&gt;parent)  g_free(t-&gt;parent);
        FREE_NAMEANDOBJ(t);
    }

    for (a = d-&gt;avps; a; a = an) {
        ddict_gavp_t* g, *gn;
        ddict_enum_t* e, *en;
        an = a-&gt;next;

        for (g = a-&gt;gavps; g; g = gn) {
            gn = g-&gt;next;
            FREE_NAMEANDOBJ(g);
        }

        for (e = a-&gt;enums; e; e = en) {
            en = e-&gt;next;
            FREE_NAMEANDOBJ(e);
        }

        if (!a-&gt;vendor)  g_free(a-&gt;vendor);
        if (!a-&gt;type)  g_free(a-&gt;type);
        if (!a-&gt;description)  g_free(a-&gt;description);
        FREE_NAMEANDOBJ(a);
    }

    g_free(d);
}</code></pre><p><br />
<br />
</p><p><strong>I wonder why we are using</strong></p><pre><code>if (!v-&gt;desc)  g_free(v-&gt;desc);
if (!t-&gt;parent)  g_free(t-&gt;parent);
if (!a-&gt;vendor)  g_free(a-&gt;vendor);
if (!a-&gt;type)  g_free(a-&gt;type);
if (!a-&gt;description)  g_free(a-&gt;description);</code></pre><p><strong>instead of using</strong></p><pre><code>if (v-&gt;desc)  g_free(v-&gt;desc);
if (t-&gt;parent)  g_free(t-&gt;parent);
if (a-&gt;vendor)  g_free(a-&gt;vendor);
if (a-&gt;type)  g_free(a-&gt;type);
if (a-&gt;description)  g_free(a-&gt;description);</code></pre><p>I think, we should use g_free to free a non-null pointer, but it seems that in the source code, we are freeing a null pointer, so what is the reason for this ?</p></div><div id="question-tags" class="tags-container tags">diameter source-code</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '16, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/78d9dce3b7a6f4e7de233c01445171c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bohao&#39;s gravatar image" /><p>bohao<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bohao has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-53285" class="comments-container"></div><div id="comment-tools-53285" class="comment-tools"></div><div class="clear"></div><div id="comment-53285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53290"></span>

<div id="answer-container-53290" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53290-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>what is the reason for this</p></blockquote><p>The reason is that somebody typed "!" when they shouldn't have. Please file a bug on this on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '16, 12:55</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></p></div></div><div id="comments-container-53290" class="comments-container"><span id="53292"></span><div id="comment-53292" class="comment"><div id="post-53292-score" class="comment-score"></div><div class="comment-text"><p>When you do, please be sure to reference this question in the bug and then report the bug number back here.</p><p>Side note: this is dead code that's never called--<code>ddict_free()</code> is never, AFAICS, called.</p></div><div id="comment-53292-info" class="comment-info"><span class="comment-age">(07 Jun '16, 13:04)</span> JeffMorriss ♦</div></div><span id="53293"></span><div id="comment-53293" class="comment"><div id="post-53293-score" class="comment-score"></div><div class="comment-text"><p>Of course I know that that main function of this file is never called unless we want to do tests. I used the compiled file "diam_dict.c" to parse the Diameter Protocol dictionary (a xml file in the source code of Wireshark) and then I found this problem. In fact, there are also some problems in the Diameter Protocol related dicitonaries (XML documents in ther directory wireshark-2.0.3/diameter), I will then report all these problems.</p></div><div id="comment-53293-info" class="comment-info"><span class="comment-age">(07 Jun '16, 13:45)</span> bohao</div></div><span id="53294"></span><div id="comment-53294" class="comment"><div id="post-53294-score" class="comment-score"></div><div class="comment-text"><p>Note that I wasn't talking about the main program but <code>ddict_free()</code>--it's not called, even by the (test) main program.</p></div><div id="comment-53294-info" class="comment-info"><span class="comment-age">(07 Jun '16, 14:10)</span> JeffMorriss ♦</div></div><span id="53297"></span><div id="comment-53297" class="comment"><div id="post-53297-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I mistook it cause I thought ddict_free() will be called in the main function and obviously it is not. Yeah, you are right, it's never called.</p></div><div id="comment-53297-info" class="comment-info"><span class="comment-age">(07 Jun '16, 14:33)</span> bohao</div></div><span id="53298"></span><div id="comment-53298" class="comment"><div id="post-53298-score" class="comment-score"></div><div class="comment-text"><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12497">Bug 12497</a>, now fixed.</p></div><div id="comment-53298-info" class="comment-info"><span class="comment-age">(07 Jun '16, 14:50)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-53290" class="comment-tools"></div><div class="clear"></div><div id="comment-53290-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

