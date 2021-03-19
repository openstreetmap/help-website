+++
type = "question"
title = "random access read and dissection of packets from a pcap file"
description = '''Hello all, I&#x27;m trying to do random access read on a growing pcap file, (program keeps track of previous EOF and then try to restart reading from this mark on growing file), for this i&#x27;m using fseek and ftell functions. But problem i&#x27;m facing is that, when i go to read the file second time ,from prev...'''
date = "2013-06-10T12:42:00Z"
lastmod = "2013-06-11T11:38:00Z"
weight = 21900
keywords = [ "development", "dissection", "pcap", "libpcap", "file" ]
aliases = [ "/questions/21900" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [random access read and dissection of packets from a pcap file](/questions/21900/random-access-read-and-dissection-of-packets-from-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21900-score" class="post-score" title="current number of votes">0</div><span id="post-21900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I'm trying to do random access read on a growing pcap file, (program keeps track of previous EOF and then try to restart reading from this mark on growing file), for this i'm using fseek and ftell functions. But problem i'm facing is that, when i go to read the file second time ,from previous EOF, pcap_open_offline shows error " bad dump file format"</p><p>how to resolve this problem? is anything wrong about my logic ?</p><p>FILE* fp=fopen(a.pcap,"r");</p><p>if(...)</p><p>fseek(fp,size,SEEK_SET);</p><p>pcap_fopen_offline(fp,errbuf);</p><p>if(..)</p><p>size=ftell(fp);</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissection" rel="tag" title="see questions tagged &#39;dissection&#39;">dissection</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '13, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p><span>Sanny_D</span><br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Jun '13, 12:43</strong> </span></p></div></div><div id="comments-container-21900" class="comments-container"></div><div id="comment-tools-21900" class="comment-tools"></div><div class="clear"></div><div id="comment-21900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21906"></span>

<div id="answer-container-21906" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21906-score" class="post-score" title="current number of votes">2</div><span id="post-21906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sanny_D has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>is anything wrong about my logic ?</p></blockquote><p>Yes. You're assuming that a <code>pcap_fopen_offline()</code> call will work regardless of whether the <code>FILE *</code> you hand to it is positioned at the beginning of the file or not; it won't, because the first thing it does is attempt to read the file header, and if it's not at the beginning of the file, it won't read the file header, it'll read whatever's at that position in the file, which might be part of the file header but not all of the file header, or might be packet data.</p><p>If you're just trying to do the moral equivalent of <code>tail -f</code> on the file - i.e., if you're reading up to an EOF, and then trying to read more packets as they're added to the file - you might just try sequentially reading; you don't need to do random access. <strong><em>HOWEVER</em></strong>, bear in mind that, unless the program <em>writing</em> to the file is being very careful to, when it writes out additional packets, write out all the packet data - for example, if it's using the standard I/O library routines to write the file (as libpcap does, and tcpdump writes its capture files out with libpcap), it must do an <code>fflush()</code> whenever it writes out a group of packets to the file. To do that with newer versions of tcpdump when run with the <code>-w</code> flag, pass it the <code>-U</code> option.</p><p>If you're really trying to do random I/O, i.e. going back and <em>rereading</em> packets, and <em>also</em> do a sequential read of the file, you should probably open the file twice, each time with <code>pcap_open_offline()</code>, and do sequential access on one <code>pcap_t</code> and random access on the other <code>pcap_t</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '13, 00:10</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-21906" class="comments-container"><span id="21923"></span><div id="comment-21923" class="comment"><div id="post-21923-score" class="comment-score"></div><div class="comment-text"><p>this is what i am trying to do, indeed i am opening the file everytym.</p><p>while(1) {</p><pre><code>    FILE *pfile=NULL;

    pfile=fopen(tmp[esc_cnt].c_str(),&quot;r&quot;);

    if((size!=0) || (size!=-1)){
            if( fseek(pfile,size,SEEK_SET)==0)
                    printf(&quot;\n fseeksizefile:%ld\n&quot;,size);fflush(stdout);

    }
    pd1 = pcap_fopen_offline(pfile, errbuf);
    printf(&quot;\nerrbuf:%s\n&quot;,errbuf);
    if(!pd1) {fflush(stdout);printf(&quot;\nNo Traffic For Selected Identities: Capture File Size Zero&quot;); fflush(stdout);
            sleep(1); esc_cnt-- ;continue;
    }

    if(pd1)
    {
            ll_type = pcap_datalink(pd1); // ll_type gloabal var
            int retval=0;
            retval = pcap_loop(pd1,-1, process_packet, NULL);

            if (retval == -1)
            {
                    pcap_perror(pd1, &quot;wshark-test: &quot;);
                    pcap_close(pd1);
                    exit(EXIT_FAILURE);

            }

            size=ftell(pfile);
            printf(&quot;\n sizefile:%ld\n&quot;,size);fflush(stdout);
    }</code></pre><p>~ ~</p></div><div id="comment-21923-info" class="comment-info"><span class="comment-age">(11 Jun '13, 04:50)</span> <span class="comment-user userinfo">Sanny_D</span></div></div><span id="21932"></span><div id="comment-21932" class="comment"><div id="post-21932-score" class="comment-score"></div><div class="comment-text"><p>Your earlier comment said</p><blockquote><p>does that mean, after opening it by pcap_open_offline then i should call fseek i.e fseek((pcap_file(pcap_t))) ?</p></blockquote><p>The answer to that is essentially "yes". Do</p><pre><code>pfile=fopen(tmp[esc_cnt].c_str(),&quot;r&quot;);
pd1 = pcap_fopen_offline(pfile, errbuf);
if((size!=0) || (size!=-1)){
        if( fseek(pfile,size,SEEK_SET)==0)
                printf(&quot;\n fseeksizefile:%ld\n&quot;,size);fflush(stdout);

}</code></pre><p>so that you do the seek <em>AFTER</em> libpcap opens the file, not <em>BEFORE</em> it opens the file.</p><p>(Also, make sure you don't keep an unlimited number of file handles open; eventually you will hit the maximum number of open files per process (most if not all UN*Xes have one; I don't know whether Windows does) and subsequent opens will fail.)</p></div><div id="comment-21932-info" class="comment-info"><span class="comment-age">(11 Jun '13, 11:38)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-21906" class="comment-tools"></div><div class="clear"></div><div id="comment-21906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

