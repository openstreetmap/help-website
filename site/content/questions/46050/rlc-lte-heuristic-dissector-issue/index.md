+++
type = "question"
title = "RLC-LTE Heuristic Dissector Issue"
description = '''Hello, I am facing difficulty while calling heuristic dissector through lua script. I am using the sample code provided at wireshark wiki for sending RLC frames over udp thenafter I am using lua to call dissector, but getting error message &quot;Can&#x27;t dissect LTE RLC frame because no per-frame info was a...'''
date = "2015-09-22T05:19:00Z"
lastmod = "2015-09-26T04:36:00Z"
weight = 46050
keywords = [ "rlc-lte" ]
aliases = [ "/questions/46050" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [RLC-LTE Heuristic Dissector Issue](/questions/46050/rlc-lte-heuristic-dissector-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46050-score" class="post-score" title="current number of votes">0</div><span id="post-46050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am facing difficulty while calling heuristic dissector through lua script. I am using the sample code provided at wireshark wiki for sending RLC frames over udp thenafter I am using lua to call dissector, but getting error message "Can't dissect LTE RLC frame because no per-frame info was attached".</p><p>I need to show the header part of rlc frames e.g RLC Mode, Direction, Logical Channel ID etc, in segregated way. <img src="https://osqa-ask.wireshark.org/upfiles/rlc-lte_roC8l76.png" alt="alt text" /></p><p>Here below the lua being used :</p><pre><code>enter code here:

do
print(&quot;hello Lua!!!&quot;)

local channel_dissectors = {
  [0] = {
    [0] = Dissector.get(&quot;rlc-lte&quot;)
  }
}

local uelog_proto = Proto(&quot;uelog&quot;,&quot;UE Log Protocol&quot;)

-- create a function to dissect it
function uelog_proto.dissector(buffer,pinfo,tree)

  local dissector = channel_dissectors[0][0]
  if dissector ~= nil then
print(&quot;Buffer %x,%x,%x \n&quot;,buffer(0,1):uint(),buffer(1,1):uint(),buffer(2,1):uint())
     --dissector:call(buffer(0):tvb(),pinfo,tree)
--pinfo.proto_data=NULL
print(&quot;Value %s&quot;,buffer(0,7):string())
pinfo.cols.info:set(buffer(0,7):string()) 
     dissector:call(buffer(7):tvb(),pinfo,tree)
  else 
     print(string.format(&quot;dissector not found, pkt number = %d&quot;, pinfo.number ))
  end

end

-- load the udp.port table
udp_table = DissectorTable.get(&quot;udp.port&quot;)
-- register our protocol to handle udp port 5001
udp_table:add(8001,uelog_proto)

end

/************************* rlc-lte Sample Code *******************************/

#include &lt;sys/types.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;netinet/in.h&gt;
#include &lt;arpa/inet.h&gt;
#include &lt;netdb.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;errno.h&gt;
#include &lt;unistd.h&gt;
#include &lt;stdint.h&gt;
#include &quot;lteRlc.h&quot;

typedef unsigned char  guint8;
typedef unsigned short guint16;
typedef unsigned int   guint32;

/* Globals where each frame is composed before sending */
static unsigned char g_PDUBuffer[16000];
static unsigned int  g_PDUOffset;
static unsigned char g_frameBuffer[16000];
static unsigned int  g_frameOffset;

/* UDP socket used for sending frames */
static int                  g_sockfd;

/* Remote serveraddress (where Wireshark is running) */
static struct sockaddr_in   g_serv_addr;

extern int rrcSockFd;
void sendLteRlcPdu();

/* Write a RLC TM PDU */
static void EncodeDummyRLCPDU1(void)
{
    g_PDUOffset = 0;

    g_PDUBuffer[g_PDUOffset++] = 0x60;
    g_PDUBuffer[g_PDUOffset++] = 0x12;
    g_PDUBuffer[g_PDUOffset++] = 0x9b;
    g_PDUBuffer[g_PDUOffset++] = 0x3e;
    g_PDUBuffer[g_PDUOffset++] = 0x9c;
    g_PDUBuffer[g_PDUOffset++] = 0xc0;
    g_PDUBuffer[g_PDUOffset++] = 0x7f;
    g_PDUBuffer[g_PDUOffset++] = 0xf0;
    g_PDUBuffer[g_PDUOffset++] = 0x96;
    g_PDUBuffer[g_PDUOffset++] = 0x64;
    g_PDUBuffer[g_PDUOffset++] = 0x30;
    g_PDUBuffer[g_PDUOffset++] = 0x64;
    g_PDUBuffer[g_PDUOffset++] = 0xcb;
    g_PDUBuffer[g_PDUOffset++] = 0x05;
    g_PDUBuffer[g_PDUOffset++] = 0x23;
    g_PDUBuffer[g_PDUOffset++] = 0xc0;
}

/* Write a RLC AM control PDU */
static void EncodeDummyRLCPDU2(void)
{
    g_PDUOffset = 0;

    g_PDUBuffer[g_PDUOffset++] = 0x00;
    g_PDUBuffer[g_PDUOffset++] = 0x04;
}

/* Write a RLC AM data PDU */
static void EncodeDummyRLCPDU3(void)
{
    g_PDUOffset = 0;

    g_PDUBuffer[g_PDUOffset++] = 0x88;
    g_PDUBuffer[g_PDUOffset++] = 0x00;
    g_PDUBuffer[g_PDUOffset++] = 0x80;
    g_PDUBuffer[g_PDUOffset++] = 0x00;
    g_PDUBuffer[g_PDUOffset++] = 0x00;
    g_PDUBuffer[g_PDUOffset++] = 0x01;
    g_PDUBuffer[g_PDUOffset++] = 0x08;
    g_PDUBuffer[g_PDUOffset++] = 0x00;
    g_PDUBuffer[g_PDUOffset++] = 0x06;
    g_PDUBuffer[g_PDUOffset++] = 0x04;
    g_PDUBuffer[g_PDUOffset++] = 0x00;
    g_PDUBuffer[g_PDUOffset++] = 0x01;
    g_PDUBuffer[g_PDUOffset++] = 0x00;
    g_PDUBuffer[g_PDUOffset++] = 0xFF;
    g_PDUBuffer[g_PDUOffset++] = 0x1D;
    g_PDUBuffer[g_PDUOffset++] = 0xA1;
    g_PDUBuffer[g_PDUOffset++] = 0x3D;
    g_PDUBuffer[g_PDUOffset++] = 0x28;
    g_PDUBuffer[g_PDUOffset++] = 0xC0;
    g_PDUBuffer[g_PDUOffset++] = 0xA8;
    g_PDUBuffer[g_PDUOffset++] = 0x00;
    g_PDUBuffer[g_PDUOffset++] = 0x01;
    g_PDUBuffer[g_PDUOffset++] = 0x00;
    g_PDUBuffer[g_PDUOffset++] = 0x00;
}

/*******************************************/
/* Add framing header to RLC PDU and send. */
void SendFrame(guint8 rlcMode, guint8 direction, guint8 priority,
               guint16 ueid, guint16 channelType, guint16 channelId,
               guint8 UMSequenceNumberLength)
{
    ssize_t bytesSent;
    g_frameOffset = 0;
    unsigned short tmp16;

    /********************************************************************/
    /* Fixed start to each frame (allowing heuristic dissector to work) */
    /* Not NULL terminated */
    memcpy(g_frameBuffer+g_frameOffset, RLC_LTE_START_STRING,
           strlen(RLC_LTE_START_STRING));
    g_frameOffset += strlen(RLC_LTE_START_STRING);

    /******************************************************************************/
    /* Now write out fixed field (the mandatory element of struct rlc_lte_info)   */
    g_frameBuffer[g_frameOffset++] = rlcMode;

    /*************************************/
    /* Now conditional fields            */

    /* UM SN length */
    if (rlcMode == RLC_UM_MODE) {
        g_frameBuffer[g_frameOffset++] = RLC_LTE_UM_SN_LENGTH_TAG;
        g_frameBuffer[g_frameOffset++] = UMSequenceNumberLength;
    }

/*************************************/
    /* Now optional fields               */

    /* Direction */
    g_frameBuffer[g_frameOffset++] = RLC_LTE_DIRECTION_TAG;
    g_frameBuffer[g_frameOffset++] = direction;

    /* Priority */
    g_frameBuffer[g_frameOffset++] = RLC_LTE_PRIORITY_TAG;
    g_frameBuffer[g_frameOffset++] = priority;

    /* UEId */
    g_frameBuffer[g_frameOffset++] = RLC_LTE_UEID_TAG;
    tmp16 = htons(ueid);
    memcpy(g_frameBuffer+g_frameOffset, &amp;tmp16, 2);
    g_frameOffset += 2;

    /* Channel Type */
    g_frameBuffer[g_frameOffset++] = RLC_LTE_CHANNEL_TYPE_TAG;
    tmp16 = htons(ueid);
    memcpy(g_frameBuffer+g_frameOffset, &amp;tmp16, 2);
    g_frameOffset += 2;

    /* Channel Id */
    g_frameBuffer[g_frameOffset++] = RLC_LTE_CHANNEL_ID_TAG;
    tmp16 = htons(ueid);
    memcpy(g_frameBuffer+g_frameOffset, &amp;tmp16, 2);
    g_frameOffset += 2;

 /***************************************/
    /* Now write the RLC PDU               */
    g_frameBuffer[g_frameOffset++] = RLC_LTE_PAYLOAD_TAG;

    /* Append actual PDU  */
    memcpy(g_frameBuffer+g_frameOffset, g_PDUBuffer, g_PDUOffset);
    g_frameOffset += g_PDUOffset;

    /* Send out the data over the UDP socket */

     printf(&quot;Sending RLC Frame over socket::::RLC Mode: %u&quot;,rlcMode);
    bytesSent = sendto(g_sockfd, g_frameBuffer, g_frameOffset, 0,(const struct sockaddr*)&amp;g_serv_addr, sizeof(g_serv_addr));
    //bytesSent = sendto(rrcSockFd, g_frameBuffer, g_frameOffset, 0,(const struct sockaddr*)&amp;g_serv_addr, sizeof(g_serv_addr));
    if (bytesSent != g_frameOffset) {
        fprintf(stderr, &quot;sendto() failed - expected %d bytes, got %d (errno=%d)\n&quot;,
                g_frameOffset, bytesSent, errno);
        exit(1);
    }
}

/*************************************************************************/
/* Main function                                                         */
/*  - set up socket + aserver address                                    */
/*  - encode and send some example LTE RLC frames using framing protocol */
int main(int argc, char *argv[])
{
    struct hostent *hp;

    if (argc &lt; 3) {
        fprintf(stderr, &quot;Usage: coclient &lt;server-host&gt; &lt;server-port&gt;\n&quot;);
        exit(1);
    }

    /***********************************/
    /* Create local socket             */
    g_sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (g_sockfd == -1) {
        fprintf(stderr, &quot;Error trying to create socket (errno=%d)\n&quot;, errno);
        exit(1);
    }

    /***************************************************/
    /* Get remote IP address from 1st command-line arg */
    g_serv_addr.sin_family = AF_INET;
    hp = gethostbyname(argv[1]);
    if (hp == (struct hostent *)0) {
        fprintf(stderr, &quot;Unknown host %s (h_errno=%d)\n&quot;, argv[1], h_errno);
        exit(1);
    }
    memcpy((void*)&amp;g_serv_addr.sin_addr, (void*)hp-&gt;h_addr, hp-&gt;h_length);

    /****************************************************/
    /* Get remote port number from 2nd command-line arg */
    g_serv_addr.sin_port = htons(atoi(argv[2]));

    /****************************************************/

//void sendLteRlcPdu()
//{

while(1){

    /* Encode and send some frames                       */
#if 0
    EncodeDummyRLCPDU1();
    SendFrame(RLC_TM_MODE,
              DIRECTION_DOWNLINK,
              0   /* Priority */,
              101 /* UEId */,
              CHANNEL_TYPE_CCCH,
              0   /* Channel Id */,
              0   /* UMSequenceNumberLength */);
#endif

    EncodeDummyRLCPDU2();
    SendFrame(RLC_AM_MODE,
              DIRECTION_UPLINK,
              1   /* Priority */,
              101 /* UEId */,
              CHANNEL_TYPE_DRB,
              3   /* Channel Id */,
              0   /* UMSequenceNumberLength */);

    EncodeDummyRLCPDU3();
    SendFrame(RLC_AM_MODE,
              DIRECTION_UPLINK,
              1   /* Priority */,
              101 /* UEId */,
              CHANNEL_TYPE_DRB,
              3   /* Channel Id */,
              0   /* UMSequenceNumberLength */);
}

    /* Close local socket */
    close(g_sockfd);

    return EXIT_SUCCESS;
}</code></pre><p>Please help me out as I am stuck at this. Any help will be appreciated</p><p>Regards Amit Kumar</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rlc-lte" rel="tag" title="see questions tagged &#39;rlc-lte&#39;">rlc-lte</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '15, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/328293431c288f04f47108594a783709?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amittkumm&#39;s gravatar image" /><p><span>amittkumm</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amittkumm has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Sep '15, 07:24</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-46050" class="comments-container"></div><div id="comment-tools-46050" class="comment-tools"></div><div class="clear"></div><div id="comment-46050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46051"></span>

<div id="answer-container-46051" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46051-score" class="post-score" title="current number of votes">0</div><span id="post-46051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If I understand your Lua code properly, you are trying to call directly the rlc-lte dissector. This will not work with the UDP framing protocol.</p><p>Instead you should let UDP dissector call the RLC-LTE over UDP heuristic dissector (after activating the heuristic dissector in RLC-LTE preferences), that will take care of filling the per frame info as requested by the framing protocol defined in epan\dissectors\packet-rlc-lte.h.</p><p>What is the purpose of your Lua dissector exactly? It seems to insert itself between the UDP and RLC-LTE dissector, preventing the per fram info to be populated.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '15, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-46051" class="comments-container"><span id="46054"></span><div id="comment-46054" class="comment"><div id="post-46054-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply and help on the same. The above snap was for testing only.</p><p>We have multiple UE connected to the system. And each UE is send the RLC packet in the UDP format , so we have added our own header above the RLC packet header to differentiate among each UE RLC packet.</p><p>In our lua script, we wanted to call the RLC-LTE dissector so that we can differentiate between UE. Could you tell me , can we directly call this RLC-LTE dissector instead of heuristic</p></div><div id="comment-46054-info" class="comment-info"><span class="comment-age">(22 Sep '15, 07:29)</span> <span class="comment-user userinfo">amittkumm</span></div></div><span id="46061"></span><div id="comment-46061" class="comment"><div id="post-46061-score" class="comment-score">1</div><div class="comment-text"><p>Yes you could, but in that case you would need to fill the rlc_lte_info structure (as found in epan\dissectors\packet-rlc-lte.h file) and attach it to pinfo, duplicating what is done in dissect_rlc_lte_heur() function. I do not know how easy this is doable in Lua (I only write C code). Be aware that the rlc_lte_info structure already contains a UE identifier, so see if it can fill your needs or not.</p></div><div id="comment-46061-info" class="comment-info"><span class="comment-age">(22 Sep '15, 10:29)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="46186"></span><div id="comment-46186" class="comment"><div id="post-46186-score" class="comment-score"></div><div class="comment-text"><p>Thanks a ton. It really helped me.</p></div><div id="comment-46186-info" class="comment-info"><span class="comment-age">(26 Sep '15, 04:36)</span> <span class="comment-user userinfo">amittkumm</span></div></div></div><div id="comment-tools-46051" class="comment-tools"></div><div class="clear"></div><div id="comment-46051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

